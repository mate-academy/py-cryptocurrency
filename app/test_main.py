from unittest import mock

from app.main import cryptocurrency_action


def test_should_return_the_higher_rate_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10.6):
        result = cryptocurrency_action(15.95)
        assert result == "Sell all your cryptocurrency"


def test_should_return_the_less_rate_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10.4):
        result = cryptocurrency_action(9.05)
        assert result == "Buy more cryptocurrency"


def test_should_return_an_equal_rate_from_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10.4):
        result = cryptocurrency_action(10)
        assert result == "Do nothing"
