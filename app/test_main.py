from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, exchange_rate, expected_result", [
    (100, 110, "Buy more cryptocurrency"),
    (100, 105, "Do nothing"),
    (90, 93, "Do nothing"),
    (100, 110.1, "Buy more cryptocurrency"),
    (100, 90, "Sell all your cryptocurrency"),
    (100, 89.9 , "Sell all your cryptocurrency"),
    (50, 110, "Buy more cryptocurrency"),
    (50, 20, "Sell all your cryptocurrency"),
    (100, 95, "Do nothing")
])
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_predict: MagicMock,
        exchange_rate: float,
        current_rate: float,
        expected_result: str) -> None:
    mock_predict.return_value = exchange_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
