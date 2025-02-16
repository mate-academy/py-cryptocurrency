from app.main import cryptocurrency_action
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),  # +6% рост
        (100, 94, "Sell all your cryptocurrency"),  # -6% падение
        (100, 105, "Do nothing"),  # +5% граница
        (100, 95, "Do nothing"),  # -5% граница
        (100, 100, "Do nothing"),  # Без изменений
    ],
)
def test_cryptocurrency_action(
    current_rate: float, predicted_rate: float, expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected, (
            f"Expected '{expected}', "
            f"but got '{result}'"
        )
