from app.main import cryptocurrency_action
from unittest import mock


def test_when_prediction_above_5_percent() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_when_prediction_is_not_that_much() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert cryptocurrency_action(96) == "Do nothing"


def test_when_prediction_below_5_percent() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=74):
        assert cryptocurrency_action(80) == "Sell all your cryptocurrency"


def test_rate_105_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"
