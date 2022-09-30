from unittest import mock
import pytest

from app.main import cryptocurrency_action as ca


@pytest.fixture()
def mocked_get_exchange():
    with mock.patch("app.main.get_exchange_rate_prediction") as \
            mocked_get_exchange:
        yield mocked_get_exchange


def test_should_call_func(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.4818
    ca(0.5)
    mocked_get_exchange.assert_called()


def test_return_buy_string(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.4818
    assert ca(0.35) == "Buy more cryptocurrency"


def test_return_sell_string(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.4818
    assert ca(0.6) == "Sell all your cryptocurrency"


def test_return_do_nothing(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.4818
    assert ca(0.5) == "Do nothing"


def test_should_not_sell(mocked_get_exchange):
    mocked_get_exchange.return_value = 1.05
    assert ca(1) == "Do nothing"


def test_shoul_not_buy(mocked_get_exchange):
    mocked_get_exchange.return_value = 0.95
    assert ca(1) == "Do nothing"
