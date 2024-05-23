from typing import Callable
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_with_large_efficient(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_with_low_efficient(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_with_equal_efficient(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
