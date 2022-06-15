from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(mocked_result):
    mocked_result.return_value = 1.06
    result = cryptocurrency_action(1)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mocked_result):
    mocked_result.return_value = 0.94
    result = cryptocurrency_action(1)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_when_ratio_is_on_the_top_margin(mocked_result):
    mocked_result.return_value = 1.05
    result = cryptocurrency_action(1)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_when_ratio_is_on_the_bottom_margin(mocked_result):
    mocked_result.return_value = 0.95
    result = cryptocurrency_action(1)
    assert result == "Do nothing"
