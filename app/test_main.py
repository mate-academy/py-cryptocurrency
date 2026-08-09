import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Callable


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Callable:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_get_exchange_rate_prediction:
        yield mock_get_exchange_rate_prediction


def test_buy(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10

    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_sell(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 2.5

    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 5 * 1.05

    assert cryptocurrency_action(5) == "Do nothing"


def test_do_nothing2(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 5 * 0.95

    assert cryptocurrency_action(5) == "Do nothing"
