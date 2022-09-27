from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_do_nothing_rate_0_95(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_rate_1_05(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_to_buy(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 20
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_to_sell(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 10
    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"
