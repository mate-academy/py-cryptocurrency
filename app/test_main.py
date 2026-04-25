from unittest import mock
from typing import Any

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        yield mocked_get_exchange_rate_prediction


def test_if_prediction_higher_than_current_rate(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_if_prediction_lower_than_current_rate(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_if_prediction_equal_current_rate(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
