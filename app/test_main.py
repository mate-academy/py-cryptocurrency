from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 9
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 11
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
