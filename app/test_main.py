from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_less_then_5_percent_down(mocked_rate_prediction):
    current_rate = 100
    mocked_rate_prediction.return_value = 95

    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_less_then_5_percent_up(mocked_rate_prediction):
    current_rate = 100
    mocked_rate_prediction.return_value = 105

    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_will_up(mocked_rate_prediction):
    current_rate = 100
    mocked_rate_prediction.return_value = 150

    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    mocked_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_will_down(mocked_rate_prediction):
    current_rate = 100
    mocked_rate_prediction.return_value = 50

    assert cryptocurrency_action(current_rate) \
           == "Sell all your cryptocurrency"
    mocked_rate_prediction.assert_called_once_with(current_rate)
