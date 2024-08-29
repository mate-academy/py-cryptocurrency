import pytest
from typing import Any
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (5, 11, "Buy more cryptocurrency"),
        (5, 2, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (1.1, 1.05, "Do nothing")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        rate_prediction_mock: Any,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    rate_prediction_mock.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
    rate_prediction_mock.assert_called_once_with(current_rate)
