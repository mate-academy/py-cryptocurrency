from typing import Any

import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, future_rate, expected",
    [
        pytest.param(100, 110, "Buy more cryptocurrency", id="more 5%"),
        pytest.param(100, 94, "Sell all your cryptocurrency", id="more 5%"),
        pytest.param(100, 105, "Do nothing", id="within 5%"),
        pytest.param(100, 95, "Do nothing", id="within 5%")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction_mock: Any,
        current_rate: [int, float],
        future_rate: [int, float],
        expected: str
) -> None:
    get_exchange_rate_prediction_mock.return_value = future_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
