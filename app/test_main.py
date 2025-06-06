from unittest import mock
from typing import Union
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, expected",
    [
        (1.15, "Buy more cryptocurrency"),
        (0.80, "Sell all your cryptocurrency"),
        (1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        exchange_rate : Union[int, float],
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange:
        mocked_get_exchange.return_value = exchange_rate
        assert cryptocurrency_action(current_rate=1) == expected
