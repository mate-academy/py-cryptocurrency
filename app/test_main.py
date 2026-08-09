from unittest import mock
from typing import Union
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected", [
        (5, 4.95, "Do nothing"),
        (1.25, 0.5, "Sell all your cryptocurrency"),
        (5, 6, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: Union[float | int],
        exchange_rate: Union[float | int],
        expected: str) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
