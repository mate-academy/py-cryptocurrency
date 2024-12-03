from typing import Callable
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_correct_result_buy(
        mock_exchange: Callable) -> None:
    mock_exchange.return_value = 100
    current_rate = 80
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_correct_result_сheck_nothing(
        mock_exchange: Callable) -> None:
    mock_exchange.return_value = 100
    current_rate = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_correct_result_sell(
        mock_exchange: Callable) -> None:
    mock_exchange.return_value = 85
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_correct_result_nothing(
        mock_exchange: Callable) -> None:
    mock_exchange.return_value = 95
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
