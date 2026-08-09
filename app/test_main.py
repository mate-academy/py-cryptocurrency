from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "function_get_exchange_rate_prediction,"
    "cryptocurrency_action_value,"
    "expect_result", [
        (1, 0.2, "Buy more cryptocurrency"),
        (1, 1.06, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing")
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_expected_result(
    mocked_get_exchange_rate_prediction: float,
    function_get_exchange_rate_prediction: float,
    cryptocurrency_action_value: Union[int, float],
    expect_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = (
        function_get_exchange_rate_prediction
    )
    result = cryptocurrency_action(cryptocurrency_action_value)
    assert result == expect_result
