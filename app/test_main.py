from unittest import mock
from .main import cryptocurrency_action


def test_buy_more_crypto() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=110.0
    ):
        assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_sell_all_crypto() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=94.0
    ):
        assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=100.0
    ):
        assert cryptocurrency_action(100.0) == "Do nothing"
