from app.main import cryptocurrency_action
from unittest import mock


@mock.patch('app.main.get_exchange_rate_prediction')
def test_should_buy_crypto(mocked_exchange):
    mocked_exchange.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_should_sell_crypto(mocked_exchange):
    mocked_exchange.return_value = 0.82
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_should_do_nothing(mocked_exchange):
    mocked_exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_should_do_nothing_too(mocked_exchange):
    mocked_exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
