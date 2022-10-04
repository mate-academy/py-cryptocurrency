from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_crypto_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_crypto_rate:
        yield mocked_crypto_rate


def test_func_should_call(mocked_crypto_rate_prediction):
    mocked_crypto_rate_prediction.return_value = 100
    cryptocurrency_action(20)
    mocked_crypto_rate_prediction.assert_called_once()


def test_buy_more_crypto(mocked_crypto_rate_prediction):
    mocked_crypto_rate_prediction.return_value = 50000
    assert cryptocurrency_action(5000) == "Buy more cryptocurrency"


def test_sell_all_crypto(mocked_crypto_rate_prediction):
    mocked_crypto_rate_prediction.return_value = 5000
    assert cryptocurrency_action(50000) == "Sell all your cryptocurrency"


def test_do_not_buy(mocked_crypto_rate_prediction):
    mocked_crypto_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_not_sell(mocked_crypto_rate_prediction):
    mocked_crypto_rate_prediction.return_value = 1
    assert cryptocurrency_action(0.95) == "Do nothing"
