import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    ("current_rate", "prediction_rate", "expected_result"),
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),

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
        assert cryptocurrency_action(current_rate) == expected_result
