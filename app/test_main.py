from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_less_then_5_percent_up(mocked):
    current_rate = 100
    mocked.return_value = 105

    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_less_then_5_percent_down(mocked):
    current_rate = 100
    mocked.return_value = 95

    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_more_than_5_percent(mocked):
    current_rate = 100
    mocked.return_value = 106

    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    mocked.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_less_than_5_percent(mocked):
    current_rate = 100
    mocked.return_value = 94
    assert cryptocurrency_action(current_rate) ==\
           "Sell all your cryptocurrency"
    mocked.assert_called_once_with(current_rate)
