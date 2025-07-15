import pytest
from app.main import cryptocurrency_action
from unittest import mock
from typing import Union


@pytest.mark.parametrize(
    "rate_prediction, current_rate, expected_result", [
        (20, 10, "Buy more cryptocurrency"),
        (5, 50, "Sell all your cryptocurrency"),
        (99, 100, "Do nothing"),
        (57.75, 55, "Do nothing"),
        (57, 60, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=rate_prediction
    ):
        assert (cryptocurrency_action(current_rate) == expected_result)
