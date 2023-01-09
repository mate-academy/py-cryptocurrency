from typing import Callable
from unittest import mock
from app.main import cryptocurrency_action

import pytest


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as test_mocked:
        yield test_mocked


def test_less_95(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_rate_95(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_more_105(mocked_rate_prediction: Callable) -> None:
    mocked_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"
