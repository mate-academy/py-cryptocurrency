from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=5):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=0.6):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=1):
        assert cryptocurrency_action(1) == "Do nothing"
