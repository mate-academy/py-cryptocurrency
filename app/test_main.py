import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 96.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected: str
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
