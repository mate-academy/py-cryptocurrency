from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> str:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.11):

        result = cryptocurrency_action(0.1)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> str:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.8):

        result = cryptocurrency_action(1.0)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> str:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=1.0):

        result = cryptocurrency_action(1.0)
        assert result == "Do nothing"


def test_should_not_buy_at_exact_1_05() -> str:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=1.05):
        result = cryptocurrency_action(1.0)
        assert result == "Do nothing"


def test_should_not_sell_at_exact_0_95() -> str:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.95):
        result = cryptocurrency_action(1.0)
        assert result == "Do nothing"
