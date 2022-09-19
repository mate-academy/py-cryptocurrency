from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.fixture()
def mocked_prediction_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") as\
            mocked_test_exchange_rate_prediction:
        yield mocked_test_exchange_rate_prediction


def test_function_was_called(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 20
    cryptocurrency_action(10)

    mocked_prediction_rate.assert_called_once()


def test_should_buy_more_cryptocurrency(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 20
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_should_sell_all_cryptocurrency(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 20
    assert cryptocurrency_action(40) == "Sell all your cryptocurrency"


def test_should_do_nothing(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 21
    assert cryptocurrency_action(20) == "Do nothing"


def test_should_do_nothing_with_rate_095(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 19
    assert cryptocurrency_action(20) == "Do nothing"
