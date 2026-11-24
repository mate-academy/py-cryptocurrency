from unittest import mock

from app import main


def test_should_buy_more_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=1.06):
        assert main.cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_sell_all_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.94):
        assert main.cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_rate_095() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.95):
        assert main.cryptocurrency_action(1) == "Do nothing"


def test_should_do_nothing_when_rate_105() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=1.05):
        assert main.cryptocurrency_action(1) == "Do nothing"
