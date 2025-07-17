from app.main import cryptocurrency_action
from unittest.mock import patch


def test_exchange_rate_more_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=2.2):
        assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_exchange_rate_equal_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.9):
        assert cryptocurrency_action(2) == "Do nothing"


def test_exchange_rate_less_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.8):
        assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_equal_lover() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=2.1):
        assert cryptocurrency_action(2) == "Do nothing"
