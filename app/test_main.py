from typing import Callable

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


def test_buy_more(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06 * 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94 * 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_get_exchange_rate_prediction: Callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05 * 100
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 0.95 * 100
    assert cryptocurrency_action(100) == "Do nothing"
