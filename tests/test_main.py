from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_more_then_5_percents_from_the_current(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 90

    assert cryptocurrency_action(85) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_less_then_5_percents_from_the_current(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 80

    assert cryptocurrency_action(85) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_within_reference(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 81

    assert cryptocurrency_action(85) == "Do nothing"
    assert cryptocurrency_action(78) == "Do nothing"
