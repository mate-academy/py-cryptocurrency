from __future__ import annotations
from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange() -> callable:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


def test_upper_bound(mock_get_exchange: callable) -> None:
    mock_get_exchange.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_lower_bound(mock_get_exchange: callable) -> None:
    mock_get_exchange.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_up(mock_get_exchange: callable) -> None:
    mock_get_exchange.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_rate_lower(mock_get_exchange: callable) -> None:
    mock_get_exchange.return_value = 80
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

