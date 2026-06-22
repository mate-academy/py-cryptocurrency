from unittest import mock

from app.main import cryptocurrency_action


def test_buy_more_when_prediction_is_higher() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=110
    ):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_when_prediction_is_lower() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=90
    ):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_equals_105_percent() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=105
    ):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_prediction_equals_95_percent() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=95
    ):
        assert cryptocurrency_action(100) == "Do nothing"
