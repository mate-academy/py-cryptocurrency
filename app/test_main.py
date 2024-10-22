import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: patch,
    current_rate: float,
    predicted_rate: float,
    expected: str
) -> None:
    mock_get_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected, f"Expected {expected}, but got {result}"
