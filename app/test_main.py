import pytest
from typing import Callable, Union
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,expected_result",
    [
        (35, 140, "Buy more cryptocurrency"),
        (44.25, 20.79, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ],
    ids=[
        "should buy more if prediction / current is good",
        "should sell all if prediction / current is low",
        "should do nothing if prediction / current is 0.95",
        "should do nothing if prediction / current is 1.05"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_returns_right_action(
        mocked_exchange_rate_prediction: Callable,
        current_rate: Union[int, float],
        prediction: Union[int, float],
        expected_result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
