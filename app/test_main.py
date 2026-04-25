from unittest.mock import patch

from app.main import cryptocurrency_action


def test_cryptocurrency_big_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=2):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_small_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.05):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_zero() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_small_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.95):
        assert cryptocurrency_action(1) == "Do nothing"
