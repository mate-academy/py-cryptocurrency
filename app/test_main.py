from unittest import mock
from typing import Callable
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Callable:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_test_rate:
        yield mock_test_rate


def test_should_call_rate_prediction(
    mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    cryptocurrency_action(100)
    mocked_get_exchange_rate_prediction.assert_called_once()
    mocked_get_exchange_rate_prediction.assert_called_once_with(100)


def test_should_return_correct_string(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    mocked_get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(0.8) == "Sell all your cryptocurrency"
    mocked_get_exchange_rate_prediction.return_value = 0.96
    assert cryptocurrency_action(0.95) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
