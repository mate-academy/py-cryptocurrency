from app.main import cryptocurrency_action
from unittest.mock import patch


def test_buy_more_cryptocurrency() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=105
    ):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("cryptocurrency.get_exchange_rate_prediction", return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=100
    ):
        assert cryptocurrency_action(100) == "Do nothing"


def test_boundary_buy() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=105.01
    ):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_boundary_sell() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=94.99
    ):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_boundary_do_nothing_high() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=105
    ):
        assert cryptocurrency_action(100) == "By more cryptocurrency"


def test_boundary_do_nothing_low() -> None:
    with patch(
            "cryptocurrency.get_exchange_rate_prediction", return_value=95
    ):
        assert cryptocurrency_action(100) == "Do nothing"
