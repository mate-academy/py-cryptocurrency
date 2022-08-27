from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_buy_more(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_sell_all(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_less_case(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_more_case(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
