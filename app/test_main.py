from typing import Any, Union
from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: Any,
    current_rate: Union[int, float],
    predicted_rate: Union[int, float],
    expected: str,
) -> None:
    mock_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
