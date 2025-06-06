from unittest import mock
from typing import Union
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current_rate, expected",
    [
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (1.06, 1, "Buy more cryptocurrency"),
        (0.90, 1, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        exchange_rate: Union[int, float],
        current_rate: Union[int, float],
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange:
        mocked_get_exchange.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == expected
