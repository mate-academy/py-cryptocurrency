from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_buy_more_cryptocurrency(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 10.2
    current_rate = 2.3
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_sell_all_cryptocurrency(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 4.1
    current_rate = 5.1
    assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_do_nothing(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 8
    current_rate = 8
    assert cryptocurrency_action(current_rate) == "Do nothing"
