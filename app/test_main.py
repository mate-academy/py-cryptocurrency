from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_price,expected_result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        exchange_rate: MagicMock,
        current_rate: int,
        predicted_price: int,
        expected_result: str
) -> None:
    exchange_rate.return_value = predicted_price
    assert cryptocurrency_action(current_rate) == expected_result
