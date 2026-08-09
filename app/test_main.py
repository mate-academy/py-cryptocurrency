from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.01):
        assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=90.0):
        assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=98.0):
        assert cryptocurrency_action(100.0) == "Do nothing"


def test_exactly_5_percent_higher() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(100.0) == "Do nothing"


def test_exactly_5_percent_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(100.0) == "Do nothing"
