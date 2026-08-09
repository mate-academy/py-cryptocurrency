from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_some_test(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
