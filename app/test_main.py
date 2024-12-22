import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_rate_95_percent_do_nothing():
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(100) == "Do nothing", (
            "You should not sell cryptocurrency when prediction_rate / current_rate == 0.95"
        )


def test_rate_105_percent_do_nothing():
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(100) == "Do nothing", (
            "You should not buy cryptocurrency when prediction_rate / current_rate == 1.05"
        )


def test_buy_more_crypto():
    with patch("app.main.get_exchange_rate_prediction", return_value=105.1):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_crypto():
    with patch("app.main.get_exchange_rate_prediction", return_value=94.9):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
