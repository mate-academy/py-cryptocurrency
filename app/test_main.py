from typing import Callable

import pytest

from unittest import mock


from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction_func() -> Callable:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_test_predict:
        yield mock_test_predict


def test_buy_more(mocked_prediction_func: Callable) -> None:
    mocked_prediction_func.return_value = 1.15
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all(mocked_prediction_func: Callable) -> None:
    mocked_prediction_func.return_value = 0.85
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_hold_savings(mocked_prediction_func: Callable) -> None:
    mocked_prediction_func.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_still_hold(mocked_prediction_func: Callable) -> None:
    mocked_prediction_func.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_prediction_func.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
