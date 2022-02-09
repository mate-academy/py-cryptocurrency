from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(prediction):
    prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
    prediction.return_value = 9.6
    assert cryptocurrency_action(10) == "Do nothing"
    prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
    prediction.return_value = 10.4
    assert cryptocurrency_action(10) == "Do nothing"
    prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
    prediction.return_value = 1.05
    assert cryptocurrency_action(1.00) == "Do nothing"
    prediction.return_value = 0.95
    assert cryptocurrency_action(1.00) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(prediction):
    prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
    prediction.return_value = 1.06
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
    prediction.return_value = 0
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(prediction):
    prediction.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
