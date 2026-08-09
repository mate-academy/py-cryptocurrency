import app.main
from app.main import cryptocurrency_action
from unittest import mock


def test_increased_prediction_rate() -> None:
    app.main.get_exchange_rate_prediction = mock.MagicMock(return_value=110)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_decreased_prediction_rate() -> None:
    app.main.get_exchange_rate_prediction = mock.MagicMock(return_value=90)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_increased_low_prediction_rate() -> None:
    app.main.get_exchange_rate_prediction = mock.MagicMock(return_value=105)
    assert cryptocurrency_action(100) == "Do nothing"


def test_decreased_low_prediction_rate() -> None:
    app.main.get_exchange_rate_prediction = mock.MagicMock(return_value=95)
    assert cryptocurrency_action(100) == "Do nothing"
