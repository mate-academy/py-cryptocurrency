import datetime
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_decrease(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.04

    assert cryptocurrency_action(1.04) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_increase(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.6

    assert cryptocurrency_action(1.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_dont_change(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 2.1

    assert cryptocurrency_action(2) == "Do nothing"
