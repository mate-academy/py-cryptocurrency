import pytest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mocked_prediction, expected_action",
    [
        (0.05, 0.7, "Buy more cryptocurrency"),
        (0.05, 0.002, "Sell all your cryptocurrency"),
        (0.05, 0.05, "Do nothing"),
        (0.10, 0.105, "Do nothing"),
        (0.10, 0.095, "Do nothing"),
        (1, 1.05, "Do nothing")

    ],
)
def test_cryptocurrency_action(current_rate: Union[int, float],
                               mocked_prediction: float,
                               expected_action: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=mocked_prediction):
        action = cryptocurrency_action(current_rate)
        assert action == expected_action
