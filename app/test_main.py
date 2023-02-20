from unittest import mock
from random import choice
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(mocked_predict):
    mocked_predict.return_value = 266 * 1.06
    assert cryptocurrency_action(266) == "Buy more cryptocurrency"
    mocked_predict.assert_called_once_with(266)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all(mocked_predict):
    mocked_predict.return_value = 266 * 0.945
    assert cryptocurrency_action(266) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing(mocked_predict):
    mocked_predict.return_value = -266 * 1.05
    assert cryptocurrency_action(-266) == "Do nothing"
    mocked_predict.return_value = -266 * 0.95
    assert cryptocurrency_action(-266) == "Do nothing"
    mocked_predict.assert_called_with(-266)
