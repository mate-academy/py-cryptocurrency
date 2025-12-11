from typing import Union
from unittest.mock import patch, Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, action",
    [
        (1.00, 1.10, "Buy more cryptocurrency"),
        (1.00, 0.90, "Sell all your cryptocurrency"),
        (1.00, 1.05, "Do nothing"),
        (1.00, 0.95, "Do nothing"),
        (1.00, 1.0501, "Buy more cryptocurrency"),
        (1.00, 0.9499, "Sell all your cryptocurrency"),
    ],
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
