import pytest
import app.main as main
from unittest.mock import patch
from app.main import cryptocurrency_action

@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_get_exchange_rate_prediction):
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 95  # Exactly 95% of current rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing", (
        "You should not sell cryptocurrency when prediction_rate / current_rate == 0.95"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_get_exchange_rate_prediction):
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 105  # Exactly 105% of current rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing", (
        "You should not buy cryptocurrency when prediction_rate / current_rate == 1.05"
    )
