from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_decreased_rate(mocked_rate: object) -> None:
    mocked_rate.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_increased_rate(mocked_rate: object) -> None:
    mocked_rate.return_value = 107
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_same_rate(mocked_rate: object) -> None:
    mocked_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_same_rate2(mocked_rate: object) -> None:
    mocked_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
