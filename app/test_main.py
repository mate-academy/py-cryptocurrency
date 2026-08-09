import pytest

from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.mark.parametrize(
    "current_exchange, exchange_rate, result",
    [(1, 1, "Do nothing"),
     (1, 1.06, "Buy more cryptocurrency"),
     (1, 0.94, "Sell all your cryptocurrency"),
     (1, 1.05, "Do nothing"),
     (1, 0.95, "Do nothing")
     ]
)
def test_cryptocurrency_action(
        exchange_rate: [int, float],
        current_exchange: float,
        result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange_rate:
        mock_exchange_rate.return_value = exchange_rate
        assert cryptocurrency_action(current_exchange) == result
