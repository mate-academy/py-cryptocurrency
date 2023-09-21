from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_nothing_to_do(exchange):
    exchange.return_value = 1.0
    assert cryptocurrency_action(1) == "Do nothing"



@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_to_do(exchange):
    exchange.return_value = 1.10
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"

@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_to_do(exchange):
    exchange.return_value = 0.93
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

@mock.patch("app.main.get_exchange_rate_prediction")
def test_nothing_to_do_when_exchange_equal_0_95(exchange):
    exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_nothing_to_do_when_exchange_equal_1_05(exchange):
    exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"