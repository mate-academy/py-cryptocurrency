from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy_more() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=110):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=90):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=100):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
