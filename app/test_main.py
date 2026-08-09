from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_crypto():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


def test_to_buy(mocked_crypto):
    mocked_crypto.return_value = 10
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_to_sell(mocked_crypto):
    mocked_crypto.return_value = 7
    assert cryptocurrency_action(9) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_crypto):
    mocked_crypto.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_for_do_not(mocked_crypto):
    mocked_crypto.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
