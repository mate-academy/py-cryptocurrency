from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_equal_current(prediction):
    prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_less_4_percent_than_current(prediction):
    prediction.return_value = 9.6
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_less_5_percent_than_current(prediction):
    prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_less_6_percent_than_current(prediction):
    prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_4_percent_than_current(prediction):
    prediction.return_value = 10.4
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_5_percent_than_current(prediction):
    prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_6_percent_than_current(prediction):
    prediction.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_equal_zero(prediction):
    prediction.return_value = 0
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_equal_1_0_6(prediction):
    prediction.return_value = 1.06
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
