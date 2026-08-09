import pytest

from typing import Union
from unittest.mock import patch, Mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_rate_predict:
        yield mocked_rate_predict


@pytest.mark.parametrize(
    "current_rate, prediction_rate, excepted, test_id",
    [
        (
            5,
            5.5,
            "Buy more cryptocurrency",
            "should buy if prediction_rate / current_rate > 1.05"
        ),
        (
            7.5,
            7,
            "Sell all your cryptocurrency",
            "should sell if prediction_rate / current_rate < 0.95"
        ),
        (
            5,
            4.75,
            "Do nothing",
            "shouldn't buy if prediction_rate / current_rate == 0.95"
        ),
        (
            5,
            5.25,
            "Do nothing",
            "shouldn't sell if prediction_rate / current_rate == 1.05"
        )
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: Mock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        excepted: str,
        test_id: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == excepted, test_id
