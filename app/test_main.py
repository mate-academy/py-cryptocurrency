import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 103, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
def test_prediction(prediction_rate: Union[float, int],
                    current_rate: Union[int, float],
                    expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected
