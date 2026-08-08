from typing import Union, Callable
from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "exchange_prediction, current_rate, expected",
    [
        (100, 10, "Buy more cryptocurrency"),
        (100, 150, "Sell all your cryptocurrency"),
        (200, 203, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (1.05, 1.0, "Do nothing")
    ]

)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: Callable,
        exchange_prediction: float,
        current_rate: Union[int, float],
        expected: str
) -> None:
    get_exchange_rate_prediction.return_value = exchange_prediction
    assert cryptocurrency_action(current_rate) == expected
