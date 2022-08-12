from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(mocked_result):
    mocked_result.return_value = 1.59
    result = cryptocurrency_action(1.5)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mocked_result):
    mocked_result.return_value = 1.49
    result = cryptocurrency_action(1.51)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mocked_result):
    mocked_result.return_value = 1.55
    result = cryptocurrency_action(1.7)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_not_sell_all_(mocked_result):
    mocked_result.return_value = 0.95
    result = cryptocurrency_action(1)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_not_buy_more_(mocked_result):
    mocked_result.return_value = 1.05
    result = cryptocurrency_action(1)
    assert result == "Do nothing"
