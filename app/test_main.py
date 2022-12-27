from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
