from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current,predicted,expected",
    [
        (10, 16, "Buy more cryptocurrency"),
        (10, 8, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing")
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
