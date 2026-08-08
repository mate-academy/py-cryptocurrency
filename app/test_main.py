from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        (80, 123.8, "Buy more cryptocurrency"),
        (200, 123.8, "Sell all your cryptocurrency"),
        (124, 123.8, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_cryptocurrency_action(current_rate: Union[int, float],
                               exchange_rate: Union[int, float],
                               result: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_exchange, mock.patch("random.choice") as mocked_choice):
        mocked_choice.return_value = "decrease"
        mocked_exchange.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
