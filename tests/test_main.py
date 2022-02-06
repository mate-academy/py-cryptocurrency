from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_more_than_5_percent_higher(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 10.6

    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_more_than_5_percent_lower(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 9.4

    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(15) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_difference_is_not_that_much(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 10

    assert cryptocurrency_action(9.6) == "Do nothing"
    assert cryptocurrency_action(10.4) == "Do nothing"
