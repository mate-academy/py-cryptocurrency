from unittest import mock

from app.main import cryptocurrency_action


def test_crypto_currency_good_prediction() -> None:
    with mock.patch("app.main.get_exchange_ra"
                    "te_prediction", return_value=5):
        assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_crypto_currency_bad_prediction() -> None:
    with mock.patch("app.main.get_exchange_"
                    "rate_prediction", return_value=5):
        assert cryptocurrency_action(6) == "Sell all your cryptocurrency"


def test_crypto_currency_do_nothing() -> None:
    with mock.patch("app.main.get_exchange"
                    "_rate_prediction", return_value=5):
        assert cryptocurrency_action(5) == "Do nothing"
