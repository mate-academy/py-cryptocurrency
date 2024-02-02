from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, result",
    [
        (2.00, "Buy more cryptocurrency"),
        (0.50, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange: mock,
        current_rate: float,
        result: str
) -> None:
    get_exchange.return_value = current_rate
    assert cryptocurrency_action(1) == result
