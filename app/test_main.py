from unittest import mock
from unittest.mock import MagicMock
from typing import Union
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        (1, 0.1, "Sell all your cryptocurrency"),
        (1, 2, "Buy more cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing")
    ],
    ids=[
        "low_rate",
        "big_rate",
        "min_do_nothing",
        "equal_to_one_do_nothing",
        "max_do_nothing",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: Union[int, float],
        exchange_rate: Union[int, float],
        expected: str
) -> None:
    mock_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
