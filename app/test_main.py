from typing import Callable
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_mock_get_exchange_rate_prediction() -> Callable:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_get_exchange_rate_prediction
    ):
        yield mock_get_exchange_rate_prediction


def test_should_buy_crypto(
        mocked_mock_get_exchange_rate_prediction: Callable,
) -> None:
    mocked_mock_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_sell_crypto(
        mocked_mock_get_exchange_rate_prediction: Callable,
) -> None:
    mocked_mock_get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_should_do_nothing_with_crypto(
        mocked_mock_get_exchange_rate_prediction: Callable,
) -> None:
    mocked_mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
