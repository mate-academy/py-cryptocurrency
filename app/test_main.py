from typing import Callable
from app.main import cryptocurrency_action, get_exchange_rate_prediction
from unittest import mock
import pytest


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


def test_buy(mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 1.0500000001
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell(mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94999999
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_high(mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_low(mocked_exchange_rate_prediction) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
