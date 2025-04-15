import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize("number, current_rate, result", [
    (0.95, 1, "Do nothing"),
    (1.06, 1, "Buy more cryptocurrency"),
    (0.90, 1, "Sell all your cryptocurrency"),
    (1.05, 1, "Do nothing")
])
def test_cryptocurrency_action(number: int, current_rate: Union[int, float],
                               result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as \
            mock_get_exchange:
        mock_get_exchange.return_value = number
        assert cryptocurrency_action(current_rate) == result
        mock_get_exchange.assert_called_once_with(current_rate)
