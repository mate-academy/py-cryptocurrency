from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mocked_func):
    current_rate = 100
    mocked_func.return_value = 110
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(mocked_func):
    current_rate = 75
    mocked_func.return_value = 70
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_func):
    current_rate = 70
    mocked_func.return_value = 72
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_95_rate(mocked_func):
    current_rate = 100
    mocked_func.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_105_rate(mocked_func):
    current_rate = 100
    mocked_func.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"

