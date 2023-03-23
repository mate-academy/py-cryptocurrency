from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_currency_when_prediction_rate_is_bad(mocked_prediction):
    mocked_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_bye_currency_when_prediction_rate_is_good(mocked_prediction):
    mocked_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_rate_medium(mocked_prediction):
    mocked_prediction.return_value = 1.001
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_1_05(mocked_prediction):
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_rate_0_95(mocked_prediction):
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"



