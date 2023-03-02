from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 1.90
    assert cryptocurrency_action(2) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_higher_rate(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 2.1
    assert cryptocurrency_action(2) == "Do nothing"
