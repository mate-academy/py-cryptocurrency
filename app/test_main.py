from typing import Generator
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> Generator:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_rate_prediction:
        yield mock_rate_prediction


@pytest.mark.parametrize(
    "rate_prediction,current_rate,expected_result",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (0.94, 1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ],
    ids=[
        "predicted rate > 5%",
        "predicted rate < 5%",
        "small difference",
        "small difference"
    ]
)
def test_cryptocurrency_action(
        mocked_rate_prediction,
        current_rate,
        rate_prediction,
        expected_result
) -> None:
    mocked_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == expected_result
