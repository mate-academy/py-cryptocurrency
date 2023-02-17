import pytest
from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,message",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ],
    ids=[
        "More than 5% higher",
        "More than 5% lower",
        "Difference is not that much",
        "Difference is not that much"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mocked_function: Callable,
        current_rate: int | float,
        prediction: int | float,
        message: str
) -> None:
    mocked_function.return_value = prediction
    assert cryptocurrency_action(current_rate) == message
