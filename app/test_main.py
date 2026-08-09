import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mocked_exchange_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_exchange_rate:
        yield mocked_exchange_rate


def test_return_sell_all_string(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_return_buy_more_string(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_return_do_nothing_string_lowest_barrier(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_return_do_nothing_string_highest_barrier(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
