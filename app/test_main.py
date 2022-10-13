from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_rate():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_patch:
        yield mocked_patch


def test_should_call_get_exchange_rate_prediction_with_arg(mocked_rate):
    mocked_rate.return_value = 12

    cryptocurrency_action(10)

    mocked_rate.assert_called_with(10)


def test_should_return_buy_if_prediction_is_1_05_or_more(mocked_rate):
    mocked_rate.return_value = 1.06

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_return_sell_if_prediction_is_0_95_or_less(mocked_rate):
    mocked_rate.return_value = 0.94

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_should_return_do_nothing_if_on_lower_border(mocked_rate):
    mocked_rate.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_if_on_higher_border(mocked_rate):
    mocked_rate.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"
