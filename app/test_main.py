import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current, expect",
    [
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (2.5, 2.1, "Buy more cryptocurrency"),
        (1.8, 0.2, "Buy more cryptocurrency"),
        (0.1, 2.1, "Sell all your cryptocurrency"),
        (10, 1, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(exchange_rate: float | int,
                               current: float | int,
                               expect: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")) as rate:
        rate.return_value = exchange_rate
        assert cryptocurrency_action(current) == expect
