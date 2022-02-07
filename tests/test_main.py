from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mocked_exchange_rate):

    mocked_exchange_rate.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mocked_exchange_rate):

    mocked_exchange_rate.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_exchange_rate):

    mocked_exchange_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_exchange_rate.return_value = 42
    assert cryptocurrency_action(40) == "Do nothing"
