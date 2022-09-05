from unittest import mock

import pytest

from app.main import cryptocurrency_action, get_exchange_rate_prediction


@pytest.fixture
def mocked_exchange():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_internal_func:
        yield mocked_internal_func


def test_internal_func_called(mocked_exchange):
    mocked_exchange.return_value = 4.0
    cryptocurrency_action(1.2)
    mocked_exchange.assert_called_once()


def test_buy_more_crypto(mocked_exchange):

    mocked_exchange.return_value = 2.0
    buy_crypto = cryptocurrency_action(1.2)
    assert buy_crypto == "Buy more cryptocurrency"


def test_sell_all_crypto(mocked_exchange):
    mocked_exchange.return_value = 1.0
    buy_crypto = cryptocurrency_action(2.0)
    assert buy_crypto == "Sell all your cryptocurrency"


def test_keep_stock(mocked_exchange):
    mocked_exchange.return_value = 9.5
    buy_crypto = cryptocurrency_action(10.0)
    assert buy_crypto == "Do nothing"


def test_keep_stock_up(mocked_exchange):
    mocked_exchange.return_value = 10.5
    buy_crypto = cryptocurrency_action(10.0)
    assert buy_crypto == "Do nothing"
