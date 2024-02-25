import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Any


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        (1.00, 1.06, "Buy more cryptocurrency"),
        (1.00, 1.05, "Do nothing"),
        (1.00, 0.95, "Do nothing"),
        (1.00, 0.94, "Sell all your cryptocurrency"),
        (1.00, 1.00, "Do nothing"),
        (1.00, 1.051, "Buy more cryptocurrency"),
        (1.00, 0.949, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Any,
        current_rate: float, predicted_rate: float,
        expected_action: str) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
