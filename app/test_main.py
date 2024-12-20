import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.01, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ],
)

def test_crypto(
    current_rate: float,
    predicted_rate: float,
    expected: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value = predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected, f"expected '{expected}' but got '{result}'."
