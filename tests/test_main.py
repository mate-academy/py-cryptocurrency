from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_bullish(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 105.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_bearish(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_in_range_more_or_less_5_percent(mocked_prediction_rate):
    mocked_prediction_rate.return_value = 10
    assert cryptocurrency_action(10.526) == "Do nothing"
    assert cryptocurrency_action(10) == "Do nothing"
    assert cryptocurrency_action(9.524) == "Do nothing"
