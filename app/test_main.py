from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(
        mocked_rate_prediction: Callable
) -> None:
    mocked_rate_prediction.return_value = 3

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all(
        mocked_rate_prediction: Callable
) -> None:
    mocked_rate_prediction.return_value = 1

    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing(
        mocked_rate_prediction: Callable
) -> None:
    mocked_rate_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"

    mocked_rate_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
