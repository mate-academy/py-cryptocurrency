from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_crypto_action():
    with mock.patch("app.main.get_exchange_rate_prediction") as \
            mock_test_crypto_action:
        yield mock_test_crypto_action


def test_function_is_called(mocked_crypto_action):
    mocked_crypto_action.return_value = 58
    cryptocurrency_action(20)
    mocked_crypto_action.assert_called_once()


def test_buy_more_crypto(mocked_crypto_action):
    mocked_crypto_action.return_value = 10
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_sell_all_crypo(mocked_crypto_action):
    mocked_crypto_action.return_value = 10
    assert cryptocurrency_action(12) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_crypto_action):
    mocked_crypto_action.return_value = 21
    assert cryptocurrency_action(20) == "Do nothing"


def test_95_percent_do_nothing(mocked_crypto_action):
    mocked_crypto_action.return_value = 19
    assert cryptocurrency_action(20) == "Do nothing"
