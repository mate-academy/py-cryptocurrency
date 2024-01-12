from app.main import cryptocurrency_action
from typing import Callable
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected_output",
    [
        (1.1, 1, "Buy more cryptocurrency"),
        (0.9, 1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_value(
        mocked_get_exchange_rate_prediction: Callable,
        exchange_rate: float,
        current_rate: int | float,
        expected_output: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_output
