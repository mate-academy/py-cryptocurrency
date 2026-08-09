from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_by_more_cryptocurrency(mocked_prediction):
    mocked_prediction.return_value = 1.65
    assert cryptocurrency_action(1.8) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_not_to_buy(mocked_prediction):
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_prediction):
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
