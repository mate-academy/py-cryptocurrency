from __future__ import annotations

from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange() -> int:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


def test_called_get_exchange(mock_get_exchange: callable) -> None:
    cryptocurrency_action(100)


def test_rate_up() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=120
    ) as exchange_rate:
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"
        exchange_rate.assert_called()


def test_rate_down() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=80
    ) as exchange_rate:
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
        exchange_rate.assert_called()


def test_rate_not_change() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=100
    ) as exchange_rate:
        assert cryptocurrency_action(100) == "Do nothing"
        exchange_rate.assert_called()
