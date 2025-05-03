from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as get_rate:
        get_rate.return_value = 1.4
        current_rate = 1
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as get_rate:
        get_rate.return_value = 0.94
        current_rate = 1
        assert cryptocurrency_action(current_rate) == ("Sell all"
                                                       " your cryptocurrency")


def test_cryptocurrency_action_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as get_rate:
        get_rate.return_value = 0.95
        current_rate = 1
        assert cryptocurrency_action(current_rate) == "Do nothing"
        get_rate.return_value = 1.05
        current_rate = 1
        assert cryptocurrency_action(current_rate) == "Do nothing"
