from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_is_more_than_5_higher(mocked_prediction):
    mocked_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_is_more_than_5_lower(mocked_prediction):
    mocked_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_difference_is_not_that_much(mocked_prediction):
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
