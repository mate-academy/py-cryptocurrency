from typing import Any
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_predicted_more_than_current(mock_pred: Any) -> None:
    mock_pred.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_predicted_less_than_current(mock_pred: Any) -> None:
    mock_pred.return_value = 100
    result = cryptocurrency_action(110)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_pred: Any) -> None:
    mock_pred.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_pred: Any) -> None:
    mock_pred.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
