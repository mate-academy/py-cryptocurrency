import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100.0, 106, "Buy more cryptocurrency"),
        (100.0, 94, "Sell all your cryptocurrency"),
        (100.0, 100, "Do nothing"),
        (100.0, 95, "Do nothing"),
        (100.0, 105, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    mock_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
