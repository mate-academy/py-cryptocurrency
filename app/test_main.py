from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=110):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=102):
        assert cryptocurrency_action(100) == "Do nothing"
