import pytest
from unittest.mock import patch
from typing import Callable
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_result", [
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 90, "Sell all your cryptocurrency"),
    (100, 110, "Buy more cryptocurrency")
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: Callable,
                               current_rate: int | float,
                               predicted_rate: int | float,
                               expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_result
