from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_exchange_rate_prediction_bigger_than_105(
        get_exchange_rate_prediction: Mock) -> None:
    get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_exchange_rate_prediction_equal_105_percent(
        get_exchange_rate_prediction: Mock) -> None:
    get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_exchange_rate_prediction_less_than_95(
        get_exchange_rate_prediction: Mock) -> None:
    get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_exchange_rate_prediction_equal_95_of_current(
        get_exchange_rate_prediction: Mock) -> None:
    get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_exchange_rate_prediction_difference_not_much(
        get_exchange_rate_prediction: Mock) -> None:
    get_exchange_rate_prediction.return_value = 104
    assert cryptocurrency_action(100) == "Do nothing"
