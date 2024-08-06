from unittest import mock
from typing import Union

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


@pytest.mark.parametrize(
    "current_rate, prediction_rate, advise",
    [
        (2, 2.2, "Buy more cryptocurrency"),
        (0.7, 0.6, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        advise: str,
        mocked_rate: mock.Mock
) -> None:
    mocked_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == advise
