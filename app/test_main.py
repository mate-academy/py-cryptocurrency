import pytest
from unittest.mock import patch, MagicMock
import app.main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),  # More than 5% higher
        (100.0, 105.0, "Do nothing"),  # Exactly 5% higher (boundary)
        (100.0, 100.0, "Do nothing"),  # No change
        (100.0, 95.0, "Do nothing"),  # Exactly 5% lower (boundary)
        (100.0, 94.0, "Sell all your cryptocurrency"),  # More than 5% lower
        (10.0, 11.0, "Buy more cryptocurrency"),  # 10% higher
        (10.0, 8.0, "Sell all your cryptocurrency"),  # 20% lower
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected: str
) -> None:
    # Set the fake predicted rate for the mocked function
    mock_get_prediction.return_value = predicted_rate

    # Call the actual function with the current rate and assert the result
    assert app.main.cryptocurrency_action(current_rate) == expected
