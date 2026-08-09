from unittest.mock import patch
from app.main import cryptocurrency_action


def test_should_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.1):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.9):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing_if_increase_within_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=104.9):
        assert cryptocurrency_action(100) == "Do nothing"


def test_should_do_nothing_if_decrease_within_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.1):
        assert cryptocurrency_action(100) == "Do nothing"


def test_boundary_exactly_5_percent_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(100) == "Do nothing"


def test_boundary_exactly_5_percent_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(100) == "Do nothing"
