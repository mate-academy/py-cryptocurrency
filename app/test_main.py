from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mocked_ex_rate: callable) -> None:
    mocked_ex_rate.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mocked_ex_rate: callable) -> None:
    mocked_ex_rate.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_do_nothing_105(mocked_ex_rate: callable) -> None:
    mocked_ex_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_95(mocked_ex_rate: callable) -> None:
    mocked_ex_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
