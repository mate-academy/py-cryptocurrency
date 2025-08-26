from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.07)
def test_rate_more_than_normal(mocked_exchange_rate: mock.Mock) -> None:
    assert cryptocurrency_action(
        current_rate=1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.02)
def test_rate_is_normal(mocked_exchange_rate: mock.Mock) -> None:
    assert cryptocurrency_action(
        current_rate=1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.8)
def test_rate_less_than_normal(mocked_exchange_rate: mock.Mock) -> None:
    assert cryptocurrency_action(
        current_rate=1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_rate_95_percent_do_nothing(mocked_exchange_rate: mock.Mock) -> None:
    assert cryptocurrency_action(
        current_rate=1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_rate_105_percent_do_nothing(mocked_exchange_rate: mock.Mock) -> None:
    assert cryptocurrency_action(
        current_rate=1) == "Do nothing"
