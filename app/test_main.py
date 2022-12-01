from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 300
    assert cryptocurrency_action(200) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 100
    assert cryptocurrency_action(200) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mocked_rate: Union[int, float]) -> None:

    mocked_rate.return_value = 200
    assert cryptocurrency_action(200) == "Do nothing"
