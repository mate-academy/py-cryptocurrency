from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_buy_more_cryptocurrency(mocked_get_exchange_rate):
    mocked_get_exchange_rate.return_value = 10.2
    assert cryptocurrency_action(2.3) ==\
           "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mocked_get_exchange_rate):
    mocked_get_exchange_rate.return_value = 4.1
    assert cryptocurrency_action(5.1) ==\
           "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_do_nothing(mocked_get_exchange_rate):
    mocked_get_exchange_rate.return_value = 8
    assert cryptocurrency_action(8) ==\
           "Do nothing"

    mocked_get_exchange_rate.return_value = 10.5
    assert cryptocurrency_action(10) == \
           "Do nothing"

    mocked_get_exchange_rate.return_value = 5.7
    assert cryptocurrency_action(6) == \
           "Do nothing"
