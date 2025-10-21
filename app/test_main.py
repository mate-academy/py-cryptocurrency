import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),   # > +5%
        (100.0, 94.0, "Sell all your cryptocurrency"),  # > -5%
        (100.0, 104.9, "Do nothing"),  # within 5%
        (100.0, 95.1, "Do nothing"),   # within 5%
        (200.0, 210.1, "Buy more cryptocurrency"),   # > +5%
        (200.0, 189.9, "Sell all your cryptocurrency"),  # > -5%
    ],
)
def test_cryptocurrency_action_with_mock(
    current_rate: float,
    predicted_rate: float,
    expected_action: str,
) -> None:
    """
    Test cryptocurrency_action with mocked prediction results.
    Ensures correct decision is made depending on rate changes.
    """
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = cryptocurrency_action(current_rate)
        assert result == expected_action
