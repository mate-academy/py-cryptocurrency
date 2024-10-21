import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=110):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_with_exactly_5_percent_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_with_exactly_5_percent_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_with_minor_variation() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=99):
        assert cryptocurrency_action(100) == "Do nothing"


if __name__ == "__main__":
    pytest.main()
