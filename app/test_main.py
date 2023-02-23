from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy(mocked: str) -> None:
    mocked.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell(mocked: str) -> None:
    mocked.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing(mocked: str) -> None:
    mocked.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mocked.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
