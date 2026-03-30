import pytest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected",
    [
        (110, 100, "Buy more cryptocurrency"),
        (106, 100, "Buy more cryptocurrency"),

        (90, 100, "Sell all your cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),

        (100, 100, "Do nothing"),
        (104, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
    ]
)
def test_prediction(prediction_rate: Union[int, float],
                    current_rate: Union[int, float],
                    expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected
