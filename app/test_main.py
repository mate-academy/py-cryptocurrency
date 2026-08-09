import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mocked_get_exchange():
    with mock.patch("app.main.get_exchange_rate_prediction") as \
            mocked_get_exchange:
        yield mocked_get_exchange


def test_should_call_func(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.98
    cryptocurrency_action(1)
    mocked_get_exchange.assert_called()


def test_return_buy_string(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.98
    assert cryptocurrency_action(0.8) == "Buy more cryptocurrency"


def test_return_sell_string(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.98
    assert cryptocurrency_action(1.2) == "Sell all your cryptocurrency"


def test_return_not_sell_and_not_buy(mocked_get_exchange):
    mocked_get_exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
