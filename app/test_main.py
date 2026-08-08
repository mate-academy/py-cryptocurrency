import pytest


from typing import Callable
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,expected_msg",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ],
    ids=[
        "test exchange rate more than 5",
        "test exchange rate less than 5",
        "test exchange rate between 5",
        "test exchange rate less than 1"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_more_than_5(mocked_prediction: Callable,
                                   prediction_rate: int | float,
                                   expected_msg: str) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(1) == expected_msg


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_get_exchange_rate_function_is_called(
    mocked_function: Callable
) -> None:
    mocked_function.return_value = 1.6
    cryptocurrency_action(1)
    mocked_function.assert_called_once()
