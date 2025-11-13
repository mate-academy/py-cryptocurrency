from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=110.0):
        assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=90.0):
        assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_do_nothing_exact_105_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(100.0) == "Do nothing"


def test_do_nothing_exact_95_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(100.0) == "Do nothing"


def test_do_nothing_middle() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=102.0):
        assert cryptocurrency_action(100.0) == "Do nothing"
