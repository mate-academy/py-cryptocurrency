from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.1):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.9):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_small_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=104.9):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_small_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.1):
        assert cryptocurrency_action(100) == "Do nothing"


def test_exact_boundaries() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(100) == "Do nothing"
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(100) == "Do nothing"
