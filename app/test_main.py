import pytest
from typing import Callable
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_rate_prediction:
        yield mock_rate_prediction


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ]
)
def test_cryptocurrency_action_result(
        mocked_rate_prediction: Callable,
        current_rate: int,
        prediction_rate: float,
        result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
