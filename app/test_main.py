from unittest import mock
from typing import Callable
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(mocked_rate: Callable) -> None:
    mocked_rate.return_value = 10600
    assert cryptocurrency_action(10000) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mocked_rate: Callable) -> None:
    mocked_rate.return_value = 9500
    assert cryptocurrency_action(10000) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_two(mocked_rate: Callable) -> None:
    mocked_rate.return_value = 10500
    assert cryptocurrency_action(10000) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mocked_rate: Callable) -> None:
    mocked_rate.return_value = 9400
    assert cryptocurrency_action(10000) == "Sell all your cryptocurrency"
