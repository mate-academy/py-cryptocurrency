from typing import Callable
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate_prediction() -> Callable:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


@pytest.mark.parametrize(
    "rate_prediction, current_rate, expected_result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (21, 20, "Do nothing"),
        (1, 2, "Sell all your cryptocurrency"),
        (19, 20, "Do nothing")
    ]
)
def test_return_correct_prediction(
        mock_rate_prediction: Callable,
        rate_prediction: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mocked_rate = mock_rate_prediction
    mocked_rate.return_value = rate_prediction

    assert cryptocurrency_action(current_rate) == expected_result
