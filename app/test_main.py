from unittest import mock
from typing import Callable

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_function() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_correct_prediction_good_rate(mocked_function: Callable) -> None:
    mocked_function.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_correct_prediction_bad_rate(mocked_function: Callable) -> None:
    mocked_function.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_correct_prediction_normal_rate(mocked_function: Callable) -> None:
    mocked_function.return_value = 0.99
    assert cryptocurrency_action(1) == "Do nothing"


def test_correct_prediction_aver_rate(mocked_function: Callable) -> None:
    mocked_function.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_correct_prediction_average_rate(mocked_function: Callable) -> None:
    mocked_function.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
