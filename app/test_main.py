from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy(mocked_exchange):
    mocked_exchange.return_value = 1.6
    result = cryptocurrency_action(100)
    mocked_exchange.assert_called_once_with(100)

    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(mocked_exchange):
    mocked_exchange.return_value = 0.8
    result = cryptocurrency_action(100)
    mocked_exchange.assert_called_once_with(100)

    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_nothing(mocked_exchange):
    mocked_exchange.return_value = 1.03
    result = cryptocurrency_action(100)
    mocked_exchange.assert_called_once_with(100)

    assert result == "Do nothing"
