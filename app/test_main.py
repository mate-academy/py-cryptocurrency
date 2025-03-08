from unittest.mock import patch
from app import main


@patch('app.main.get_exchange_rate_prediction')
def test_rate_95_percent_do_nothing(mock_get_prediction: patch):
    mock_get_prediction.return_value = 95
    current_rate = 100

    result = main.cryptocurrency_action(current_rate)

    assert result == "Do nothing", f"Expected \"Do nothing\" but got {result}"


@patch('app.main.get_exchange_rate_prediction')
def test_rate_105_percent_do_nothing(mock_get_prediction: patch):
    mock_get_prediction.return_value = 105
    current_rate = 100

    result = main.cryptocurrency_action(current_rate)

    assert result == "Do nothing", f"Expected \"Do nothing\" but got {result}"
