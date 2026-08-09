import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("predicted_rate, expected_action", [
    (1.06, "Buy more cryptocurrency"),
    (0.94, "Sell all your cryptocurrency"),
    (1.02, "Do nothing"),
    (1.05, "Do nothing"),
    (0.95, "Do nothing"),
])
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        predicted_rate: float,
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == expected_action
