from unittest import mock
from .main import cryptocurrency_action


def test_buy_more_crypto() -> None:
    with mock.patch("app.main.get_market_change", return_value=71.5):
        result = cryptocurrency_action()
        assert result == "Buy more cryptocurrency"


def test_sell_all_crypto() -> None:
    with mock.patch("app.main.get_market_change", return_value=11.5):
        result = cryptocurrency_action()
        assert result == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch("app.main.get_market_change", return_value=35.0):
        result = cryptocurrency_action()
        assert result == "Do nothing"
