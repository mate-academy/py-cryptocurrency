from unittest import mock
from typing import Any, Callable

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_exchange_rate_prediction):
        yield mock_exchange_rate_prediction


def test_exchange_rate_prediction_called(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 40.1
    cryptocurrency_action(20)
    mocked_exchange_rate_prediction.assert_called_once_with(20)


def test_response_buy(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 40
    assert cryptocurrency_action(31) == "Buy more cryptocurrency"


def test_response_sell(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 12.96
    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


def test_response_do_nothing(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 15.01
    assert cryptocurrency_action(15) == "Do nothing"


def test_response_do_nothing_95_rate(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_response_do_nothing_105_rate(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
