from unittest import mock
from typing import Callable

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "inp,result,message",
    [
        (1, 1.12, "Buy more cryptocurrency"),
        (1, 0.76, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mocked_func: Callable,
        inp: int,
        result: float,
        message: str) -> None:
    mocked_func.return_value = result
    assert cryptocurrency_action(inp) == message
