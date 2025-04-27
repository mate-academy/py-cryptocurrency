from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange: (int, float),
        current_rate: (int, float),
        exchange_rate: (int, float),
        result: str) -> None:
    mock_exchange.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result
