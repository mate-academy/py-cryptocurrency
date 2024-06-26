from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Any


@pytest.mark.parametrize(
    "possible_rate, expected_result",
    [
        (120, "Buy more cryptocurrency"),
        (80, "Sell all your cryptocurrency"),
        (103, "Do nothing"),
        (97, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: Any,
        possible_rate: int,
        expected_result: str
) -> None:
    get_exchange_rate_prediction.return_value = possible_rate
    assert cryptocurrency_action(100) == expected_result
