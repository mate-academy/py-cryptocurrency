from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_is_more(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 29.68

    assert cryptocurrency_action(28) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_is_less(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 23.5

    assert cryptocurrency_action(25) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_is_slightly_higher(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 105.01

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_is_slightly_lower(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 94.99

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_upper_limit_indicator(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_lower_limit_indicator(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"
