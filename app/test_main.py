from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_minor_down_changes(
        test_rate_prediction: Callable) -> None:
    test_rate_prediction.return_value = 1.9
    assert cryptocurrency_action(2) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_minor_up_changes(
        test_rate_prediction: Callable) -> None:
    test_rate_prediction.return_value = 2
    assert cryptocurrency_action(1.9) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_if_predicted_rate_higher(
        test_rate_prediction: Callable) -> None:
    test_rate_prediction.return_value = 5
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_if_predicted_rate_lower(
        test_rate_prediction: Callable) -> None:
    test_rate_prediction.return_value = 1
    assert cryptocurrency_action(3.0) == "Sell all your cryptocurrency"
