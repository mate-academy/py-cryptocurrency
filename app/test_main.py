from unittest import mock
from app import main


def test_second_should_do_nothing_with_cryptocurrency()\
        -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=1.05
    ):
        result = main.cryptocurrency_action(1)
        assert result == "Do nothing"


def test_should_do_nothing_with_cryptocurrency()\
        -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=0.95
    ):
        result = main.cryptocurrency_action(1)
        assert result == "Do nothing"


def test_should_return_buy_crypto_if_exchange_rate_more_than_2() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=2
    ):
        result = main.cryptocurrency_action(1)
        assert result == "Buy more cryptocurrency"


def test_should_return_sell_crypto_if_exchange_rate_less_than_1() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=0.5
    ):
        result = main.cryptocurrency_action(1)
        assert result == "Sell all your cryptocurrency"
