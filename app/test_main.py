from app.main import cryptocurrency_action
from unittest.mock import patch


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.1):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.9):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper_bound() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_bound() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"
