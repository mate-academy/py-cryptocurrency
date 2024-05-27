from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current,predicted,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
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
