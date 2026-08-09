from typing import Callable
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_105(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 13.65
    assert cryptocurrency_action(13) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_95(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 12.35
    assert cryptocurrency_action(13) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_cryptocurrency(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 14.1
    assert cryptocurrency_action(13.3) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_cryptocurrency(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 12.5
    assert cryptocurrency_action(13.3) == "Sell all your cryptocurrency"
