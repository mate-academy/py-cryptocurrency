from typing import Union
from unittest.mock import patch, Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 101, "Do nothing"),
        (101, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_parametrized(
    mock_get_exchange_rate_prediction: Mock,
    current_rate: Union[int, float],
    exchange_rate: Union[int, float],
    action: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate

    result = cryptocurrency_action(current_rate)

    assert result == action
