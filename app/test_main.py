import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    current_rate = 100
    predicted_rate = 106.01

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    current_rate = 100
    predicted_rate = 94.99

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"


def test_rate_105_percent_do_nothing() -> None:
    current_rate = 100
    predicted_rate = 105

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    current_rate = 100
    predicted_rate = 95

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_do_nothing_increase() -> None:
    current_rate = 100
    predicted_rate = 104

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_do_nothing_decrease() -> None:
    current_rate = 100
    predicted_rate = 96

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"


if __name__ == "__main__":
    pytest.main()
