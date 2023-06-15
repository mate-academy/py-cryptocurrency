from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_buy_more_if_good_prediction(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 3
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_sell_all_if_bad_prediction(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_do_nothing_if_small_difference(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.5
    assert cryptocurrency_action(2) == "Do nothing"

    mocked_exchange_rate_prediction.return_value = 2.5
    assert cryptocurrency_action(2) == "Do nothing"
