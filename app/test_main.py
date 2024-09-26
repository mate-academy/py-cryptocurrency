from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_test():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_test:
        yield mock_test


def test_to_buy(mocked_test):
    mocked_test.return_value = 10
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_to_sell(mocked_test):
    mocked_test.return_value = 2
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


def test_to_do_nothing(mocked_test):
    mocked_test.return_value = 5.25
    assert cryptocurrency_action(5) == "Do nothing"


def test_to_do_nothing_again(mocked_test):
    mocked_test.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"
