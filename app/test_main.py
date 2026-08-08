from unittest import mock
from typing import Callable


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test(mocked_exchange: Callable) -> None:
    mocked_exchange.return_value = 1.1
    result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"

    mocked_exchange.return_value = 0.9
    result = cryptocurrency_action(1.0)
    assert result == "Sell all your cryptocurrency"

    mocked_exchange.return_value = 1.05
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"

    mocked_exchange.return_value = 0.95
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"
