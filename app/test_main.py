from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mocked_function):
    mocked_function.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_function.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_buy(mocked_function):
    mocked_function.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_to_sell(mocked_function):
    mocked_function.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
