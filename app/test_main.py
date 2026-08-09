from unittest import mock

from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent__do_nothing(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent__do_nothing(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_lees_then_95_percent_sell_all(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_more_then_105_percent_buy_more(
        mocked_prediction: Union[int, float]
) -> None:
    mocked_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"
