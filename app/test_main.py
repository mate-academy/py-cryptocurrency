import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: patch,
        current_rate: int,
        predicted_rate: int,
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
    mock_get_exchange_rate_prediction.assert_called_with(current_rate)
