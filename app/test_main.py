from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        (100.0, 105.1, "Buy more cryptocurrency"),  # > 5% increase
        (100.0, 105.0, "Do nothing"),  # Exactly 5% increase
        (100.0, 100.0, "Do nothing"),  # No change
        (100.0, 95.0, "Do nothing"),  # Exactly 5% decrease
        (100.0, 94.9, "Sell all your cryptocurrency"),  # > 5% decrease
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_scenarios(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_action: str
) -> None:
    # Set the mock to return our test's predicted rate
    mock_prediction.return_value = predicted_rate

    # Assert the function returns the correct string
    assert cryptocurrency_action(current_rate) == expected_action
