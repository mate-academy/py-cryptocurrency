import pytest
from typing import Callable
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_rate_prediction:
        yield mock_rate_prediction


def test_get_exchange_rate_prediction_has_been_called(
        mocked_rate_prediction: Callable
) -> None:
    mocked_rate_prediction.return_value = 100
    cryptocurrency_action(99)
    mocked_rate_prediction.assert_called_once_with(99)


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 30, "Sell all your cryptocurrency"),
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
