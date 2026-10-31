from unittest.mock import MagicMock, patch
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 94.0, "Sell all your cryptocurrency"),
        (100, 102.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    current_rate: int,
    predicted_rate: float,
    expected: str,
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
