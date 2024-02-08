import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_action",
    [
        (1.05, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (1.0, 1.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    predicted_rate: float,
    current_rate: float,
    expected_action: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
    assert result == expected_action, (f"Expected {expected_action}, "
                                       f"but got {result}.")


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_action",
    [
        (1.10, 1.0, "Buy more cryptocurrency"),
        (0.90, 1.0, "Sell all your cryptocurrency"),
        (1.0, 1.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action_boundary_cases(
    predicted_rate: float,
    current_rate: float,
    expected_action: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
    assert result == expected_action, (f"Expected {expected_action}, "
                                       f"but got {result}.")
