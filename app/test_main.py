from unittest import mock

from app.main import cryptocurrency_action


def test_border_action_not_buy() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_border_action_not_sell() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"


def test_case_buy_more_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=3):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_case_sell_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=1):
        assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_case_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=3):
        assert cryptocurrency_action(3) == "Do nothing"
