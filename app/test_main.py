from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more_crypto() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=110.0
    ):
        result = cryptocurrency_action(100.0)
        assert result == "Buy more cryptocurrency"


def test_sell_all_crypto() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=94.0
    ):
        result = cryptocurrency_action(100.0)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_normal() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=103.0
    ):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=105.0
    ):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=95.0
    ):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
