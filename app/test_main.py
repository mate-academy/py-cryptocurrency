import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_action",
    [
        (105, 100, "Buy more cryptocurrency"),
        (95, 100, "Sell all your cryptocurrency"),
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
    ],
)
def test_cryptocurrency_action(predicted_rate: Union[int, float],
                               current_rate: Union[int, float],
                               expected_action: str) -> None:
    with patch("main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected_action
