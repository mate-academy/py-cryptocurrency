from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_good_prediction_rate(mocked_get_exchange_rate_prediction:
                              Union[int, float]) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.10
    result = cryptocurrency_action(1.00)
    assert (result == "Buy more cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_bad_prediction_rate(mocked_get_exchange_rate_prediction:
                             Union[int, float]) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.90
    result = cryptocurrency_action(1.00)
    assert (result == "Sell all your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_no_actions_lower_bound(mocked_get_exchange_rate_prediction:
                                Union[int, float]) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    result = cryptocurrency_action(1.00)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_no_actions_upper_bound(mocked_get_exchange_rate_prediction:
                                Union[int, float]) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1.00)
    assert result == "Do nothing"
