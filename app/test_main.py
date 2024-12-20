import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
        (100, 105, "Do nothing")
    ],
)

def test_crypto(
    current_rate: int,
    predicted_rate: int,
    expected: int
) -> None:
    with (patch("app.main.get_exchange_rate_prediction",
               return_value = predicted_rate)):
        result = cryptocurrency_action(current_rate)
        assert result == expected, f"expected '{expected}' but got '{result}'."
