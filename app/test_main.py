from unittest import mock
from typing import Callable
import app.main
import pytest


@pytest.mark.parametrize(
    "rate, result", [
        (0.5, "Sell all your cryptocurrency"),
        (1.5, "Buy more cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: Callable,
        rate: int | float,
        result: str
) -> None:
    mocked_rate_prediction.return_value = rate
    assert app.main.cryptocurrency_action(1) == result
