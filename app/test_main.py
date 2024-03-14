from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Union


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (1, 1.051, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.949, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        assert cryptocurrency_action(
            current_rate
        ) == expected_result
