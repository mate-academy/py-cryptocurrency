from pytest import mark
from typing import Callable
from unittest import mock

from app.main import cryptocurrency_action


@mark.parametrize(
    "predicted_rate, message",
    [
        (1.10, "Buy more cryptocurrency"),
        (0.9, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ],
    ids=[
        "predicted_rate_essentially_more_than_current",
        "predicted_rate_essentially_less_than_current",
        "predicted_rate_not_essentially_more_than_current",
        "predicted_rate_not_essentially_less_than_current",
    ]
)
@mock.patch(
    "app.main.get_exchange_rate_prediction",
)
def test_returning_correct_message(
        mocked_prediction: Callable[[int, float], str],
        predicted_rate: float,
        message: str
) -> None:
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(1) == message
