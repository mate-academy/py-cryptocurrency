from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.1):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.9):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_within_range() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=102):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_exactly_105_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_exactly_95_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
