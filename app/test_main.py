from typing import Callable
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        pytest.param(1.1, 1.0, "Buy more cryptocurrency"),
        pytest.param(0.9, 1.0, "Sell all your cryptocurrency"),
        pytest.param(0.95, 1.0, "Do nothing"),
        pytest.param(1.05, 1.0, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_prediction: Callable,
                               current_rate: float,
                               prediction_rate: float,
                               expected_result: str) -> None:
    mock_get_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
