from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 110.0, "Buy more cryptocurrency"),
        (100, 94.0, "Sell all your cryptocurrency"),
        (100, 90.0, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 102.5, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    mock_get_prediction,
    current_rate,
    predicted_rate,
    expected_result
):
    mock_get_prediction.return_value = predicted_rate
    
    result = cryptocurrency_action(current_rate)
    
    assert result == expected_result
    mock_get_prediction.assert_called_once_with(current_rate)
