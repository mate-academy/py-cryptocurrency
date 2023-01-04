from unittest import mock
from typing import Callable
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate() -> Callable:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_exchange_rate:
        yield mocked_exchange_rate


def test_prediction_rate_less_95_percent(
        mocked_exchange_rate: Callable
) -> None:
    mocked_exchange_rate.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_prediction_rate_95_percent(
        mocked_exchange_rate: Callable
) -> None:
    mocked_exchange_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_prediction_rate_more_105_percent(
        mocked_exchange_rate: Callable
) -> None:
    mocked_exchange_rate.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_prediction_rate_105_percent(
        mocked_exchange_rate: Callable
) -> None:
    mocked_exchange_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
