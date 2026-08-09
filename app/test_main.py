from typing import Any
from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_value, expected",
    [
        (100.0, 110.0, "Buy more cryptocurrency"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
        (100.0, 103.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.01, "Buy more cryptocurrency"),
        (100.0, 94.99, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_scenarios(
    mock_predict: Any,
    current_rate: float,
    prediction_value: float,
    expected: str,
) -> None:
    mock_predict.return_value = prediction_value
    assert cryptocurrency_action(current_rate) == expected
