from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_prediction() -> mock.MagicMock:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_test_prediction
    ):
        yield mock_test_prediction


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        pytest.param(
            100.0,
            106.0,
            "Buy more cryptocurrency",
            id="predicted rate is 5% more than the current one"
        ),
        pytest.param(
            100.0,
            105.0,
            "Do nothing",
            id="predicted rate is exactly 5% more than the current one"
        ),
        pytest.param(
            100.0,
            100.0,
            "Do nothing",
            id="predicted rate is equal to the current rate"
        ),
        pytest.param(
            100.0,
            95.0,
            "Do nothing",
            id="predicted rate is exactly 5% less than the current one"
        ),
        pytest.param(
            100.0,
            90.0,
            "Sell all your cryptocurrency",
            id="predicted rate is 5% less than the current one"
        ),
        pytest.param(
            100.0,
            0,
            "Sell all your cryptocurrency",
            id="predicted rate equal 0"
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_prediction: mock.MagicMock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
