from unittest.mock import patch
from app.main import cryptocurrency_action


def test_rate_95_percent_do_nothing() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=95.0):
        assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=105.0):
        assert cryptocurrency_action(100) == "Do nothing"


def test_buy_more_crypto() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=105.1):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_crypto() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=94.9):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
