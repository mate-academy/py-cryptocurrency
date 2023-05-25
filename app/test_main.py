from unittest import mock

from typing import Any

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_with_106_rate(mocked_get_exchange_rate_prediction: Any) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_with_1_rate(mocked_get_exchange_rate_prediction: Any) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_with_095_rate(mocked_get_exchange_rate_prediction: Any) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_with_105_rate(mocked_get_exchange_rate_prediction: Any) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_with_094_rate(mocked_get_exchange_rate_prediction: Any) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
