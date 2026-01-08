from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    mock_get_rate: MagicMock,
    current_rate: int,
    predicted_rate: int,
    expected_action: str
) -> None:
    mock_get_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
