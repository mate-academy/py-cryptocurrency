import pytest

from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (3, 2, "Buy more cryptocurrency"),
        (2, 3, "Sell all your cryptocurrency"),
        (2.1, 2, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (2, 2, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: Any,
        prediction_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    print(mocked_prediction.return_value)
    action = cryptocurrency_action(current_rate)
    print(action)
    assert action == expected_result
