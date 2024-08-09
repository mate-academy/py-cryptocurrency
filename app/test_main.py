from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    current_rate = 100
    prediction_rate = 106
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    current_rate = 100
    prediction_rate = 94
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    current_rate = 100
    prediction_rate = 96
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == "Do nothing"
