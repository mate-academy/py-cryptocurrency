from typing import Union

from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, result, message",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.64, "Buy more cryptocurrency"),
        (1, 2, "Buy more cryptocurrency"),
        (1, 0.46, "Sell all your cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.03, "Do nothing"),
        (1, 0.97, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_message(
        mocked_func: mock,
        current_rate: Union[int, float],
        result: int | float,
        message: str) -> None:
    mocked_func.return_value = result
    assert cryptocurrency_action(current_rate) == message
