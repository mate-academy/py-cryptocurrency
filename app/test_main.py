import pytest
from app.main import cryptocurrency_action

# Test cases for cryptocurrency_action function


@pytest.mark.parametrize("current_rate, expected_action", [
    (100, "Buy more cryptocurrency"),  # Predicted rate > 5% increase
    (95, "Sell all your cryptocurrency"),  # Predicted rate > 5% decrease
    (98, "Do nothing"),  # Predicted rate < 5% decrease
    (100, "Do nothing"),  # Predicted rate is equal to current rate
])
def test_cryptocurrency_action(
        current_rate: int,
        expected_action: float
) -> None:
    assert cryptocurrency_action(current_rate) == expected_action
