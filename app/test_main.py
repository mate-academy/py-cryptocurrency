# write your code he
import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action

# Тест для сценария "Buy more cryptocurrency"
def test_buy_more() -> None:
    current_rate = 100

    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(current_rate)
    
    assert result == "Buy more cryptocurrency"


# Тест для сценария "Sell all your cryptocurrency"
def test_sell_all() -> None:
    current_rate = 100

    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(current_rate)
    
    assert result == "Sell all your cryptocurrency"


# Тест для сценария "Do nothing"
def test_do_nothing() -> None:
    current_rate = 100

    with patch("app.main.get_exchange_rate_prediction", return_value=103):
        result = cryptocurrency_action(current_rate)
    
    assert result == "Do nothing"


# Граничные случаи (точно ±5%)
def test_exactly_5_percent_higher() -> None:
    current_rate = 100

    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(current_rate)
    
    assert result == "Do nothing"


def test_exactly_5_percent_lower() -> None:
    current_rate = 100

    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(current_rate)
    
    assert result == "Do nothing"
