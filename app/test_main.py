from typing import Callable
from unittest.mock import patch


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_buy_more(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 20
    result = cryptocurrency_action(4)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_sell_all(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    result = cryptocurrency_action(2)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_when_prediction_equal_to_top_range(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_when_prediction_equal_to_bot_range(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    result = cryptocurrency_action(1)
    assert result == "Do nothing"
