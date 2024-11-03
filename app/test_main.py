from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=106
    ):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=90
    ):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=102
    ):
        assert cryptocurrency_action(100) == "Do nothing"
