from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=110)
def test_higher_crypto_rate(mocked_prediction: callable) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=90)
def test_lower_crypto_rate(mocked_prediction: callable) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=100)
def test_do_nothing_crypto_rate(mocked_prediction: callable) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_do_nothing_high_crypto_rate(mocked_prediction: callable) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_do_nothing_low_crypto_rate(mocked_prediction: callable) -> None:
    assert cryptocurrency_action(100) == "Do nothing"
