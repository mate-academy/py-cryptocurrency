import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_cryptocurrency_action_returns_correct_values(
        current_rate: int | float,
        predicted_rate: int | float,
        expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
