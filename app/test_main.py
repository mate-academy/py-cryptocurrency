from typing import Callable
from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 85, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: Callable,
        current_rate: int,
        prediction: int,
        result: str
) -> None:
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == result
