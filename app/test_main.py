from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_higher_current(mocked_prediction):
    mocked_prediction.return_value = 6
    assert cryptocurrency_action(5.60) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_lower_current(mocked_prediction):
    mocked_prediction.return_value = 6
    assert cryptocurrency_action(6.40) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_exchange_rate_in_range_current(mocked_prediction):
    mocked_prediction.return_value = 6
    assert cryptocurrency_action(6) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_equal_105(mocked_prediction):
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_equal_95(mocked_prediction):
    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
