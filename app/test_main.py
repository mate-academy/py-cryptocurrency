import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Callable


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> int or float:
    with patch("app.main.get_exchange_rate_prediction") as mock_exc_rate:
        yield mock_exc_rate


def test_buy_more(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_rate_95(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_rate_105(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
