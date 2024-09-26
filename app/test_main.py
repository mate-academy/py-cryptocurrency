import pytest
from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> Callable:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


def test_exchange_rate_more_five(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.09
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.90
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_one_more(
        mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
