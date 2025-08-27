from unittest.mock import patch
from app.main import cryptocurrency_action


def test_exchange_rate_5_proc_higher() -> None:
    current_rate = 100
    predicted_rate = 106
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_exchange_rate_5_proc_lower() -> None:
    current_rate = 100
    predicted_rate = 94
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"


def test_exactly_5_percent_higher() -> None:
    current_rate = 100
    predicted_rate = 105
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_exactly_5_percent_lower() -> None:
    current_rate = 100
    predicted_rate = 95
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
