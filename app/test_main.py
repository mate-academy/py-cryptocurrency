from unittest import mock
# from typing import Callable

import pytest

# import app.main
from app.main import get_exchange_rate_prediction, cryptocurrency_action

"""
@pytest.mark.parametrize(
    "prediction,current,result",
    [
        pytest.param(
            10,
            8,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency case"
        ),
        pytest.param(
            8,
            10,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency case"
        ),
        pytest.param(
            10,
            10,
            "Do nothing",
            id="Do nothing case"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: mock,
                               prediction: int | float,
                               current: int | float,
                               result: str) -> None:
    mock_get_exchange_rate_prediction.result_value = prediction
    assert cryptocurrency_action(current) == result
"""


@pytest.fixture()
def mocked_get_exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        yield mocked_func


def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: int | float):
    current = 10
    mocked_get_exchange_rate_prediction.result_value = 8
    assert cryptocurrency_action(current) == "Buy more cryptocurrency"


def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: int | float):
    current = 8
    mocked_get_exchange_rate_prediction.result_value = 10
    assert cryptocurrency_action(current) == "Sell all your cryptocurrency"


def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: int | float):
    current = 10
    mocked_get_exchange_rate_prediction.result_value = 10
    assert cryptocurrency_action(current) == "Do nothing case"
