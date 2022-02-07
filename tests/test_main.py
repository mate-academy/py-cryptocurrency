from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 10
    assert cryptocurrency_action(11) == "Sell all your cryptocurrency"
    mocked_exchange_rate.return_value = 15
    assert cryptocurrency_action(16.5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_by_more_cryptocurrency(mocked_exchange_rate):

    mocked_exchange_rate.return_value = 11
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
    mocked_exchange_rate.return_value = 12
    assert cryptocurrency_action(11) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 17.5
    assert cryptocurrency_action(17) == "Do nothing"
    mocked_exchange_rate.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
