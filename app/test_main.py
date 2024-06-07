from __future__ import annotations
from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current,predicted,expected",
    [
        (1.1, 2.8, "Buy more cryptocurrency"),
        (3.6, 2.1, "Sell all your cryptocurrency"),
        (2.1, 2.2, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current: int | float,
        predicted: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as exchange:
        exchange.return_value = predicted
        assert cryptocurrency_action(current) == expected
