import pytest
from typing import Union

from app.main import cryptocurrency_action

from unittest.mock import patch


@pytest.mark.parametrize(
    "current_exchange, exchange, action",
    [(1, 1, "Do nothing"),
     (1, 1.05, "Do nothing"),
     (1, 0.95, "Do nothing"),
     (1, 1.06, "Buy more cryptocurrency"),
     (1, 0.94, "Sell all your cryptocurrency")
     ])
def test_cryptocurrency_action(
        exchange: Union[int, float],
        current_exchange: float,
        action: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange_rate:
        mock_exchange_rate.return_value = exchange
        assert cryptocurrency_action(current_exchange) == action
