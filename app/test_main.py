import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 104.99, "Do nothing"),
    (100, 95.01, "Do nothing"),
    (100, 100, "Do nothing"),
])
def test_cryptocurrency_action(
        current_rate: int,
        predicted_rate: int | float,
        expected_action: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected_action
