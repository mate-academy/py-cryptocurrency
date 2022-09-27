from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


def test_should_return_buy_more(mocked_func):
    mocked_func.return_value = 110

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_return_sell(mocked_func):
    mocked_func.return_value = 90

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_return_do_nothing(mocked_func):
    mocked_func.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"

    mocked_func.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"
