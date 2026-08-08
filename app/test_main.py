from typing import Any
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_return",
    [
        pytest.param(
            3, 1, "Buy more cryptocurrency",
            id="return buy more cryptocurrency"
        ),

        pytest.param(
            0.5, 0.7, "Sell all your cryptocurrency",
            id="return sell all"
        ),

        pytest.param(
            6.3, 6, "Do nothing",
            id="return do nothing if prediction = 1.05"
        ),

        pytest.param(
            7.6, 8, "Do nothing",
            id="return do nothing if prediction = 0.95"
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_prediction: Any,
        prediction_rate: float,
        current_rate: int | float,
        expected_return: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_return
    mocked_prediction.assert_called_once_with(current_rate)
