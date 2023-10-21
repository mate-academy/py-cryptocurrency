import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy_cryptocurrency_action(mocked_get_exchange_rate_prediction) -> None:

    mocked_get_exchange_rate_prediction.return_value = 1.15
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell_cryptocurrency_action(mocked_get_exchange_rate_prediction) -> None:

    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_action(mocked_get_exchange_rate_prediction) -> None:

    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing2_action(mocked_get_exchange_rate_prediction) -> None:

    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
