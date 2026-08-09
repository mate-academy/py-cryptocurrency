import unittest.mock
from typing import Union
from unittest.mock import MagicMock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate_value, prediction_rate_value, result",
    [
        pytest.param(100.0, 100.0, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),
        pytest.param(100, 94, "Sell all your cryptocurrency"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(100.0, 106.0, "Buy more cryptocurrency")
    ],
    ids=[
        "Float type with a nominal case value 100",
        "Integer type and a value (95) just above the boundary 0.95",
        "Integer type and a value (94) just bellow the boundary 0.95",
        "Integer type and a value (105) just bellow the boundary 1.05",
        "Float type and a value (106.0) just above the boundary 1.05",
    ]
)
@unittest.mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_various_conditions(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate_value: Union[int, float],
        prediction_rate_value: float,
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate_value
    assert cryptocurrency_action(current_rate_value) == result
