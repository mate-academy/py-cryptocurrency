from app.main import cryptocurrency_action
from unittest import mock
from typing import Callable

import pytest


@pytest.mark.parametrize(
    "befor_random, res_rate, message",
    [
        (1, 1.07, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ],
    ids=[
        "if rate -> 1.07 <- must return -> 'Buy more cryptocurrency' <-",
        "if rate -> 0.94 <- must return -> 'Sell all your cryptocurrency' <-",
        "if rate -> 1.05 <- must return -> 'Do nothing' <-",
        "if rate -> 0.95 <- must return -> 'Do nothing' <-",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction(
    mocked_func: Callable,
    befor_random: int,
    res_rate: float,
    message: int
) -> None:
    mocked_func.return_value = res_rate
    assert cryptocurrency_action(befor_random) == message
