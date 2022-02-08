from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_growth_higher_five_percent(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(0.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_decline_lower_five_percent(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1.5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_difference_is_not_that_much(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1.05) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
