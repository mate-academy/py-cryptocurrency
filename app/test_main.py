from unittest import mock
import pytest
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "curr_rate, exchange_rate_val, expected_result",
    [
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05000001, "Buy more cryptocurrency"),
        (1, 999, "Buy more cryptocurrency"),
        (1, 0.94999999, "Sell all your cryptocurrency"),
        (1, 0, "Sell all your cryptocurrency"),
        (1, -1, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock.MagicMock,
        curr_rate: Union[int, float],
        exchange_rate_val: Union[int, float],
        expected_result: str
) -> None:
    mocked_exchange_rate.return_value = exchange_rate_val
    assert cryptocurrency_action(curr_rate) == expected_result
