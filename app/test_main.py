from typing import Any
from unittest import mock

import pytest

import app.main

current_rate = 5


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Any:
    with mock.patch("app.main.get_exchange_rate_prediction"
                    ) as mocked_get_exchange_rate_prediction:
        yield mocked_get_exchange_rate_prediction


def test_get_exchange_rate_prediction_has_been_called_with(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 4
    app.main.cryptocurrency_action(current_rate)
    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)


def test_cryptocurrency_action_buy_if_greater_by_more_than_5_percent(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 5.26
    result = app.main.cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_if_smaller_by_more_than_5_percent(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 4.74
    result = app.main.cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing_if_no_difference(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 5
    result = app.main.cryptocurrency_action(current_rate)

    assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing_if_greater_by_5_percent(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 5.25
    result = app.main.cryptocurrency_action(current_rate)

    assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing_if_smaller_by_5_percent(
        mocked_get_exchange_rate_prediction: Any) -> Any:
    mocked_get_exchange_rate_prediction.return_value = 4.75
    result = app.main.cryptocurrency_action(current_rate)

    assert result == "Do nothing"
