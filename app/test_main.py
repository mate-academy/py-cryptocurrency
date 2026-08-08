from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_get_prediction:
        yield mocked_get_prediction


def test_when_prediction_increase(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 178.23
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_when_prediction_decrease(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 12.00
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_when_prediction_105(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_when_prediction_95(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
