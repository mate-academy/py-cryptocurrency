from unittest import mock
from typing import Callable
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_cryptocurrency(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 210
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 95
    assert cryptocurrency_action(100.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_two_do_nothing(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 105
    assert cryptocurrency_action(100.0) == "Do nothing"
