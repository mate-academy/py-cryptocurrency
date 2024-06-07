import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch('app.main.get_exchange_rate_prediction')
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch('app.main.get_exchange_rate_prediction')
def test_buy_sell_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch('app.main.get_exchange_rate_prediction')
def test_nothing(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 98
    assert cryptocurrency_action(100) == "Do nothing"


@patch('app.main.get_exchange_rate_prediction')
def test_rate_95_percent_do_nothing(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@patch('app.main.get_exchange_rate_prediction')
def test_rate_105_percent_do_nothing(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
