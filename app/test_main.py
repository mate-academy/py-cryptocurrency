import pytest

from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_output",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 108, "Buy more cryptocurrency"),
        (100, 91, "Sell all your cryptocurrency"),
        (100, 80, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_exchange_rate_prediction: MagicMock,
        current_rate: int,
        predicted_rate: int,
        expected_output: str
) -> None:
    mock_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_output
