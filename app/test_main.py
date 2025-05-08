from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


def test_should_buy_more_when_predicted_rate_is_high() -> None:
    current_rate = 100
    predicted_rate = 106

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_should_sell_all_when_rate_is_low() -> None:
    current_rate = 100
    predicted_rate = 94

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"


@pytest.mark.parametrize("multiplier", [
    0.95, 0.96, 0.97, 0.98, 0.99,
    1.00, 1.01, 1.02, 1.03, 1.04, 1.05
])
def test_should_do_nothing(multiplier: float) -> None:
    current_rate = 100
    predicted_rate = current_rate * multiplier

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
