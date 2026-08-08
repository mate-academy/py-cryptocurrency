from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate, return_value, result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
    ]
)
def test_if_exchange_higher(
        rate: float,
        return_value: float,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = return_value
        assert cryptocurrency_action(rate) == result
