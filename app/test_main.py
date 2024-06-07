from __future__ import annotations
from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        pytest.param(
            3.05, 2, "Sell all your cryptocurrency",
            id="Rate fall"
        ),
        pytest.param(
            1.25, 5, "Buy more cryptocurrency",
            id="Rate rise"
        ),
        pytest.param(
            49.99, 52, "Do nothing",
            id="Close values"
        ),
        pytest.param(
            52, 49.99, "Do nothing",
            id="Close values"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: callable,
        current_rate: int | float,
        prediction_rate: int | float,
        expected_result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result