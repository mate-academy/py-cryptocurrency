import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action

@pytest.mark.parametrize("current_rate, prediction_rate, result", [
    (1, 1.2, "Buy more cryptocurrency"),
    (1, 0.65, "Sell all your cryptocurrency"),
    (1, 1.05, "Do nothing"),
    (1, 0.95, "Do nothing")
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction, current_rate, prediction_rate, result):
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == result
