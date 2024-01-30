import pytest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_exchange, exchange_rate, expected_result",
    [
        pytest.param(1, 0.9, "Sell all your cryptocurrency",
                     id="Sell all your cryptocurrency test"),
        pytest.param(1, 0.95, "Do nothing",
                     id="Do nothing test"),
        pytest.param(1, 1.05, "Do nothing",
                     id="Do nothing test"),
        pytest.param(1, 1.06, "Buy more cryptocurrency",
                     id="Buy more cryptocurrency test")
    ]
)
def test_cryptocurrency_action(
    exchange_rate: Union[int, float],
    current_exchange: Union[int, float],
    expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange_rate:
        mock_exchange_rate.return_value = exchange_rate
        assert cryptocurrency_action(current_exchange) == expected_result
