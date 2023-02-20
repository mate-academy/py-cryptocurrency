from typing import Union, Callable
from unittest import mock

import pytest

from app.main import get_exchange_rate_prediction, cryptocurrency_action


@pytest.mark.parametrize(
    "current, prediction, action",
    [
        pytest.param(
            100, 105, "Do nothing",
            id="if difference is not that much"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="if difference is not that much"
        ),
        pytest.param(
            15.102, 15.86, "Buy more cryptocurrency",
            id="prediction is 5% higher from the current.",
        ),
        pytest.param(
            15.102, 14.03, "Sell all your cryptocurrency",
            id="prediction is 5% lower from the current."
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_correct_action(
        mocked_get_exchange: Callable,
        current: Union[int, float],
        prediction: Union[int, float],
        action: str
) -> None:
    mocked_get_exchange.return_value = prediction
    assert cryptocurrency_action(current) == action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_was_called(mocked_get_exchange: Callable) -> None:
    mocked_get_exchange.return_value = 49.15
    cryptocurrency_action(19.24)
    mocked_get_exchange.assert_called_once()


def test_random_was_called() -> None:
    with mock.patch("random.random") as mocked_random:
        get_exchange_rate_prediction(3.48)
        mocked_random.assert_called_once()
