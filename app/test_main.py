from typing import Callable
from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    prediction_rate: Callable,
    prediction: int | float,
    current: int | float,
    expected: str
) -> None:
    prediction_rate.return_value = prediction
    assert cryptocurrency_action(current) == expected
