from typing import Callable

import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


def test_cryptocurrency_action_buy_more_cryptocurrency(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all_your_cryptocurrency(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_do_nothing_2(
        mocked_exchange_rate_prediction: Callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
