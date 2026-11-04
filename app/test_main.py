from unittest.mock import patch
import pytest
from typing import Any

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 105.0, "Do nothing"),
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 95.0, "Do nothing"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_calculate_expected_result(
        mocked_get_exchange_rate_prediction: Any,
        current_rate: int | float, prediction_rate: int | float,
        expected_result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected_result

    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)
