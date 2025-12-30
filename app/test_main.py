from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mocked_exchange):
    mocked_exchange.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_less_cryptocurrency(mocked_exchange):
    mocked_exchange.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_exchange):
    mocked_exchange.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rating_is_095(mocked_exchange):
    mocked_exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rating_is_1_05(mocked_exchange):
    mocked_exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
