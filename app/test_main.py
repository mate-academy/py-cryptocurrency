from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        yield mocked_prediction


def test_get_more_cryptocurrency(
        mocked_exchange_rate_prediction: callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 5
    assert (
        cryptocurrency_action(2) == "Buy more cryptocurrency"
    ), "You should buy more cryptocurrency" \
       " when prediction_rate / current_rate == 1.05"


def test_sell_all_cryptocurrency(
        mocked_exchange_rate_prediction: callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 3
    assert (
        cryptocurrency_action(4) == "Sell all your cryptocurrency"
    ), "You should sell all your cryptocurrency" \
       " when prediction_rate / current_rate == 0,75"


def test_do_nothing_105_percent(
        mocked_exchange_rate_prediction: callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 2.1
    assert (
        cryptocurrency_action(2) == "Do nothing"
    ), "You should do nothing when prediction_rate / current_rate == 1.05"


def test_do_nothing_95_percent(
        mocked_exchange_rate_prediction: callable
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.9
    assert (
        cryptocurrency_action(2) == "Do nothing"
    ), "You should do nothing when prediction_rate / current_rate == 0.95"
