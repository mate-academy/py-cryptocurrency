import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: float,
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    # Mock the return value of get_exchange_rate_prediction
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    # Call the function
    result = cryptocurrency_action(current_rate)

    # Assert the expected result
    assert result == expected_action
