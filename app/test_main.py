from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_105(mocked_get_exchange):
    mocked_get_exchange.return_value = 2.1
    assert cryptocurrency_action(2) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_095(mocked_get_exchange):
    mocked_get_exchange.return_value = 1.9
    assert cryptocurrency_action(2) == "Do nothing"
