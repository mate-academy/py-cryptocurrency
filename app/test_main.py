from unittest.mock import patch
from typing import Callable
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_can_sell_cryptocurrency(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_can_buy_more_cryptocurrency(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_get_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
