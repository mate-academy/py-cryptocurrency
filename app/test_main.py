from unittest.mock import patch
from typing import Union
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    mock_prd: object,
    current_rate: Union[int, float],
    predicted_rate: Union[int, float],
    expected: str
) -> None:
    mock_prd.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
