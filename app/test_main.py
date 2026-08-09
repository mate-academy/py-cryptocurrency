from unittest.mock import patch
import app.main as main


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert main.cryptocurrency_action(100) == (
            "Sell all your cryptocurrency"
        )


def test_do_nothing_inside() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=100):
        assert main.cryptocurrency_action(100) == "Do nothing"


def test_boundary_plus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert main.cryptocurrency_action(100) == "Do nothing"


def test_boundary_minus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert main.cryptocurrency_action(100) == "Do nothing"
