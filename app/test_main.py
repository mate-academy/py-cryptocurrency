from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 120.0, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 80.0, "Sell all your cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: patch,
    current_rate: int | float,
    prediction_rate: int | float,
    expected_action: str,
) -> None:
    mock_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_action
    mock_prediction.assert_called_once_with(current_rate)
