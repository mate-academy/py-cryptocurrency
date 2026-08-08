from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_increase_much_more_than_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 150):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_increase_little_more_than_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 106):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_increase_is_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_decrease_is_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 95):
        assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_decrease_much_less_than_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 50):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_decrease_little_less_than_5() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", lambda a: 94):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
