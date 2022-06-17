from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_growing(mocked_rate_of_prediction):
    current_rate = 123
    mocked_rate_of_prediction.return_value = 200
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"

    mocked_rate_of_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_falling(mocked_rate_of_prediction):
    current_rate = 123
    mocked_rate_of_prediction.return_value = 60
    assert cryptocurrency_action(current_rate) \
           == "Sell all your cryptocurrency"

    mocked_rate_of_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_5_percents_more(mocked_rate_of_prediction):
    current_rate = 100
    mocked_rate_of_prediction.return_value = 105
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mocked_rate_of_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_5_percents_less(mocked_rate_of_prediction):
    current_rate = 100
    mocked_rate_of_prediction.return_value = 95
    assert cryptocurrency_action(current_rate) == "Do nothing"
