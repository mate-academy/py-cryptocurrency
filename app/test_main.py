from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected_result: str,
) -> None:
    mock_get_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_result
    mock_get_prediction.assert_called_once_with(current_rate)
