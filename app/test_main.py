from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),      # 6% higher (> 5%)
        (100, 94, "Sell all your cryptocurrency"),  # 6% lower (> 5%)
        (100, 105, "Do nothing"),                   # Exactly 5% higher
        (100, 95, "Do nothing"),                    # Exactly 5% lower
        (100, 100, "Do nothing"),                   # Equal rates
        (200, 212, "Buy more cryptocurrency"),      # 6% higher of 200
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    """Test cryptocurrency_action with various rate predictions."""
    mock_get_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected
