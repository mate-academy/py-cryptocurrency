import pytest

from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_ex_rate_prediction() -> int:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
    ) as mock_exchange_rate:
        yield mock_exchange_rate


@pytest.mark.parametrize(
    "ex_rate, cur_rate, result",
    [
        (10, 5, "Buy more cryptocurrency"),
        (1, 1.1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ],
    ids=[
        "test 1: should return 'Buy more cryptocurrency'",
        "test 2: should return 'Sell all your cryptocurrency'",
        "test 3: should return 'Do nothing'",
        "test 4: should return 'Do nothing'"
    ]
)
def test_cryptocurrency_action(
        ex_rate: int | float,
        cur_rate: int | float,
        result: str,
        mock_ex_rate_prediction: Callable
) -> None:
    mock_ex_rate_prediction.return_value = ex_rate
    with mock_ex_rate_prediction:
        assert (
            cryptocurrency_action(cur_rate) == result
        )
