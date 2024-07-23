import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ],
    ids=[
        "6% increase, buy",
        "6% decrease, sell",
        "5% increase, just wait",
        "5% decrease, just wait"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
