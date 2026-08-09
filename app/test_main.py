from unittest import mock
from typing import Callable

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_exchange_rate_prediction, current_rate, expected",
    [
        pytest.param(
            100,
            10,
            "Buy more cryptocurrency",
            id="when rate prediction is higher than current rate"
        ),
        pytest.param(
            100,
            150,
            "Sell all your cryptocurrency",
            id="when rate prediction is lover than current rate"
        ),
        pytest.param(
            200,
            202,
            "Do nothing",
            id="when difference rate prediction and current rate is small"
        ),
        pytest.param(
            10.5,
            10,
            "Do nothing",
            id="when prediction rate larger by 5%"
        ),
        pytest.param(
            9.5,
            10,
            "Do nothing",
            id="when current rate larger by 5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: Callable,
        mock_exchange_rate_prediction: int,
        current_rate: int,
        expected: str
) -> None:
    get_exchange_rate_prediction.return_value = mock_exchange_rate_prediction
    assert cryptocurrency_action(current_rate) == expected
