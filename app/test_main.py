import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch

# Test when the predicted exchange rate is more than 5% higher
@patch('app.main.get_exchange_rate_prediction')
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

# Test when the predicted exchange rate is more than 5% lower
@patch('app.main.get_exchange_rate_prediction')
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

# Test when the difference in predicted exchange rate is within 5%
@patch('app.main.get_exchange_rate_prediction')
def test_do_nothing(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"

