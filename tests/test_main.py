from unittest import mock
from app.main import cryptocurrency_action


@mock.patch('app.main.get_exchange_rate_prediction')
def test_call_to_buy_cryptocurrency(mock_exchange_rate):
    mock_exchange_rate.return_value = 11
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_call_to_sell_cryptocurrency(mock_exchange_rate):
    mock_exchange_rate.return_value = 9
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_call_to_hold_cryptocurrency(mock_exchange_rate):
    mock_exchange_rate.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
