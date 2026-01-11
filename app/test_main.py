from typing import Any
from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_get_prediction):
    mock_get_prediction.return_value = 106.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_get_prediction):
    mock_get_prediction.return_value = 94.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mock_get_prediction):
    mock_get_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"
