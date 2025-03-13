from typing import Any
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_need_to_buy(prediction: Any) -> None:
    exchange_rate = 1
    mock.MagicMock.return_value = 1.9
    assert cryptocurrency_action(exchange_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_need_to_sell(prediction: Any) -> None:
    exchange_rate = 3
    mock.MagicMock.return_value = 1.9
    assert (cryptocurrency_action(exchange_rate)
            == "Sell all your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_not_much_difference(prediction: Any) -> None:
    exchange_rate = 2
    mock.MagicMock.return_value = 1.9
    assert cryptocurrency_action(exchange_rate) == "Do nothing"
    exchange_rate = 1
    mock.MagicMock.return_value = 1
    assert cryptocurrency_action(exchange_rate) == "Do nothing"
    exchange_rate = 2
    mock.MagicMock.return_value = 2.1
    assert cryptocurrency_action(exchange_rate) == "Do nothing"
