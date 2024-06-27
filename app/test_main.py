import pytest
from unittest.mock import patch
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: patch,
    current_rate: Union[int, float],
    prediction_rate: float,
    expected_action: str
) -> None:
    mock_prediction.return_value = prediction_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected_action
