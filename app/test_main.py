from unittest.mock import Mock, patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 94.0, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: Mock,
    current_rate: Mock,
    predicted_rate: int,
    expected: str,
) -> None :
    mock_get_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected

    mock_get_prediction.assert_called_once_with(current_rate)
