from unittest import mock

import pytest

from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_predicted() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        yield mocked_func


def test_should_propose_to_buy_action(
        mocked_get_exchange_rate_predicted: Callable
) -> None:
    mocked_get_exchange_rate_predicted.return_value = 2.1 * 5
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_should_propose_to_do_nothing_action(
        mocked_get_exchange_rate_predicted: Callable
) -> None:
    mocked_get_exchange_rate_predicted.return_value = 0.95 * 635
    assert cryptocurrency_action(635) == "Do nothing"

    mocked_get_exchange_rate_predicted.return_value = 1.05 * 100
    assert cryptocurrency_action(100) == "Do nothing"


def test_should_propose_to_sell_action(
        mocked_get_exchange_rate_predicted: Callable
) -> None:
    mocked_get_exchange_rate_predicted.return_value = 0.1 * 378.09
    assert cryptocurrency_action(378.09) == "Sell all your cryptocurrency"
