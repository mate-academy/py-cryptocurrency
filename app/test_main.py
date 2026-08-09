from __future__ import annotations
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, future_rate, expected_action",
    [
        pytest.param(
            1.00,
            1.06,
            "Buy more cryptocurrency",
            id="test predicated exchange rate "
               "is more than 5% higher from current"
        ),
        pytest.param(
            1.00,
            1.05,
            "Do nothing",
            id="test if difference in 5% or less to UP"
        ),
        pytest.param(
            1.00,
            0.95,
            "Do nothing",
            id="test if difference in 5% or less to DOWN"
        ),
        pytest.param(
            1.00,
            0.94,
            "Sell all your cryptocurrency",
            id="test predicated exchange rate "
               "is more than 5% lower from current"
        )
    ]
)
def test_cryptocurrency_action(
        current_rate: float | int,
        future_rate: float | int,
        expected_action: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = future_rate
        assert cryptocurrency_action(
            current_rate=current_rate
        ) == expected_action
