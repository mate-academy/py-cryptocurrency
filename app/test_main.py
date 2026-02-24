import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        # More than +5%
        (100.0, 106.0, "Buy more cryptocurrency"),

        # Exactly +5% (boundary)
        (100.0, 105.0, "Do nothing"),

        # Less than -5%
        (100.0, 94.0, "Sell all your cryptocurrency"),

        # Exactly -5% (boundary)
        (100.0, 95.0, "Do nothing"),

        # Small positive change
        (100.0, 103.0, "Do nothing"),

        # Small negative change
        (100.0, 98.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action_scenarios(
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == expected
