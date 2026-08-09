import pytest
from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "mocked_return_value, current_value, expected_message",
    [
        (4.75, 5, "Do nothing"),
        (5.25, 5, "Do nothing")
    ]
)
def test_should_return_sell_all(
        mocked_get_exchange: Any,
        mocked_return_value: int | float,
        current_value: int | float,
        expected_message: str
) -> None:
    mocked_get_exchange.return_value = mocked_return_value
    assert cryptocurrency_action(current_value) == expected_message
