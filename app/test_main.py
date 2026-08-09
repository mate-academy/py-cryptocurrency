from typing import Union
import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104.99, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate: Union[int, float],
    predicted_rate: Union[int, float],
    expected: str
) -> None:
    """Test all possible actions with mocked prediction."""
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected
