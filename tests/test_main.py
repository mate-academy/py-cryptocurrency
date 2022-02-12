from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predicated_exchange_rate_bigger_then_5(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1

    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predicated_exchange_rate_lower_than_5(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 2

    assert cryptocurrency_action(1.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predicated_exchange_rate_difference_low(mocked_exchange_rate):
    mocked_exchange_rate.return_value = 1.05

    assert cryptocurrency_action(1.0) == "Do nothing"
