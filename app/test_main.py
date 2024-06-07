from __future__ import annotations
from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        pytest.param(
            3.05, 2, "Buy more cryptocurrency",
            id="Rate rise"
        ),
        pytest.param(
            1.25, 5, "Sell all your cryptocurrency",
            id="Rate fall"
        ),
        pytest.param(
            49.99, 52, "Do nothing",
            id="Close values"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: mock.MagicMock,
        prediction_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
