from typing import Any
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        yield mocked_prediction


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (10, 11, "Sell all your cryptocurrency"),
        (11, 10, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (100, 100, "Do nothing")
    ]
)
def test_prediction_rate(
        mocked_get_exchange_rate_prediction: Any,
        prediction_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mocked_prediction = mocked_get_exchange_rate_prediction
    mocked_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
