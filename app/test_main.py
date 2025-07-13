from app.main import cryptocurrency_action
from unittest.mock import patch


def test_exchange_rate_more_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=15):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_exchange_rate_equal_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"


def test_exchange_rate_less_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.94):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
