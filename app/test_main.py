from typing import Callable
from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.1)
def test_buy(mock_prediction: Callable) -> None:
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.9)
def test_sell(mock_prediction: Callable) -> None:
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_do_nothing_lower(mock_prediction: Callable) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_do_nothing_upper(mock_prediction: Callable) -> None:
    assert cryptocurrency_action(1) == "Do nothing"
