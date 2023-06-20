import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency():
    with patch('app.main.get_exchange_rate_prediction',
               return_value=105.0):
        result = cryptocurrency_action(100.0)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency():
    with patch('app.main.get_exchange_rate_prediction',
               return_value=94.0):
        result = cryptocurrency_action(100.0)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing():
    with patch('app.main.get_exchange_rate_prediction',
               return_value=100.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"


def test_boundary_buy():
    with patch('app.main.get_exchange_rate_prediction',
               return_value=105.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"  # Exactly 5% increase


def test_boundary_sell():
    with patch('app.main.get_exchange_rate_prediction',
               return_value=95.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"  # Exactly 5% decrease
