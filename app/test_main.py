from unittest.mock import patch
from app.main import cryptocurrency_action


def test_high_rate() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=105):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_medium_rate() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=100):
        assert cryptocurrency_action(100) == "Do nothing"


def test_low_rate() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=95):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
