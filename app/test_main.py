from unittest import mock

from app.main import cryptocurrency_action


def test_should_return_the_less_rate_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=12):
        result = cryptocurrency_action(10)
        assert result == "Buy more cryptocurrency"


def test_should_return_the_higher_rate_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=8):
        result = cryptocurrency_action(10)
        assert result == "Sell all your cryptocurrency"


def test_should_return_an_equal_rate_from_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10.2):
        result = cryptocurrency_action(10)
        assert result == "Do nothing"


def test_should_return_an_equal_rate_from_current2() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10.5):
        result = cryptocurrency_action(10)
        assert result == "Do nothing"


def test_should_return_an_equal_rate_from_current3() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=9.5):
        result = cryptocurrency_action(10)
        assert result == "Do nothing"
