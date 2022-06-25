from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_you_buy_more_crypto(mocked_prediction):
    mocked_prediction.return_value = 1
    assert cryptocurrency_action(0.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_you_sell_more_crypto(mocked_prediction):
    mocked_prediction.return_value = 1
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_1(mocked_prediction):
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_2(mocked_prediction):
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
