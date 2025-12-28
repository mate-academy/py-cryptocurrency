from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=104):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"

    with mock.patch("app.main.get_exchange_rate_prediction", return_value=96):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
