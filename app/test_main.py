from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_buy() -> None:
    get_exchange_rate_prediction = mock.MagicMock()
    get_exchange_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_do_nothing() -> None:
    get_exchange_rate_prediction = mock.MagicMock()
    get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(0.95) == "Do nothing"


def test_cryptocurrency_sell() -> None:
    get_exchange_rate_prediction = mock.MagicMock()
    get_exchange_rate_prediction.return_value = 0.8
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
