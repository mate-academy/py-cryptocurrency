import pytest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result", [
        (100, 106, "Buy more cryptocurrency"),
        (300, 284, "Sell all your cryptocurrency"),
        (500, 500, "Do nothing"),
        (600, 595, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(current_rate: int,
                               prediction_rate: Union[int, float],
                               result: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == result
