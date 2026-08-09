import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, action",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        mocked_func: Union,
        current_rate: int,
        predicted_rate: int,
        action: str
) -> None:
    mocked_func.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == action
