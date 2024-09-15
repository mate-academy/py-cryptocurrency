from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_case_less(mocked_crypto):
    mocked_crypto.return_value = 0.95
    rez = cryptocurrency_action(1)
    assert rez == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_case_more(mocked_crypto):
    mocked_crypto.return_value = 1.05
    rez = cryptocurrency_action(1)
    assert rez == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_by_more(mocked_crypto):
    mocked_crypto.return_value = 1.7
    rez = cryptocurrency_action(0.71)
    assert rez == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell_all(mocked_crypto):
    mocked_crypto.return_value = 1.12
    rez = cryptocurrency_action(1.7)
    assert rez == "Sell all your cryptocurrency"
