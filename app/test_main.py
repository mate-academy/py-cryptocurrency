from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 80
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mocked_get_rate: mock) -> None:
    mocked_get_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
