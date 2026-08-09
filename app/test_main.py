from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> int | float:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


def test_when_prediction_rate_is_high(mocked_rate: int) -> None:
    mocked_rate.return_value = 1.06

    result = cryptocurrency_action(1)

    assert result == "Buy more cryptocurrency"


def test_when_prediction_rate_is_low(mocked_rate: int) -> None:
    mocked_rate.return_value = 0.94

    result = cryptocurrency_action(1)

    assert result == "Sell all your cryptocurrency"


def test_when_prediction_rate_is_095(mocked_rate: int) -> None:
    mocked_rate.return_value = 0.95

    result = cryptocurrency_action(1)

    assert result == "Do nothing"


def test_when_prediction_rate_is_105(mocked_rate: int) -> None:
    mocked_rate.return_value = 1.05

    result = cryptocurrency_action(1)

    assert result == "Do nothing"
