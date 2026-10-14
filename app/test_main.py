from unittest.mock import patch, MagicMock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 120.0, "Buy more cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 104.9, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 95.1, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 94.9, "Sell all your cryptocurrency"),
        (100.0, 80.0, "Sell all your cryptocurrency"),
        (1.0, 1.0501, "Buy more cryptocurrency"),
        (1.0, 0.9499, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)
