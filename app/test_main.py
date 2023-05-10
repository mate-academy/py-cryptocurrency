from unittest import mock
from .main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with mock.patch("get_exchange_rate_prediction", lambda: 5):
        assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch("get_exchange_rate_prediction", lambda: 0.6):
        assert cryptocurrency_action(0.6) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_nothing() -> None:
    with mock.patch("get_exchange_rate_prediction", lambda: 1):
        assert cryptocurrency_action(1) == "Do nothing"
