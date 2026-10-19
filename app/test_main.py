from unittest import mock

from app.main import cryptocurrency_action


def test_should_get_message_buy_6_percents_great() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=106
    ):
        assert cryptocurrency_action(
            100
        ) == "Buy more cryptocurrency"


def test_should_get_message_sell_6_percents_less() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=94
    ):
        assert cryptocurrency_action(
            100
        ) == "Sell all your cryptocurrency"


def test_should_get_message_nothing_2_percents_less() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=98
    ):
        assert cryptocurrency_action(
            100
        ) == "Do nothing"


def test_should_get_message_nothing_5_percents_less() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=95
    ):
        assert cryptocurrency_action(
            100
        ) == "Do nothing"


def test_should_get_message_nothing_5_percents_greate() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=105
    ):
        assert cryptocurrency_action(
            100
        ) == "Do nothing"


def test_should_get_message_buy_50_percent_greater() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=150
    ):
        assert cryptocurrency_action(
            100
        ) == "Buy more cryptocurrency"


def test_should_get_message_sell_30_percent_less() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
            return_value=70
    ):
        assert cryptocurrency_action(
            100
        ) == "Sell all your cryptocurrency"
