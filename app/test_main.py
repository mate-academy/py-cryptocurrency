from collections.abc import Callable
from unittest import mock
from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 120.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 80.0, "Sell all your cryptocurrency"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: Callable,
        current_rate: float,
        prediction_rate: float,
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
