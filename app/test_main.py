from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_currency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_currency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_rate_95_percent_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
