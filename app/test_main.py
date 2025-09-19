from unittest.mock import patch, Mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 102, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: Mock,
                               current_rate: int,
                               predicted_rate: int,
                               expected_action: str
                               ) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
