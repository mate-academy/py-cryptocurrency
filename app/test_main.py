from app.main import cryptocurrency_action
from unittest import mock


def test_should_return_buy_more_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=1.07):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_return_sell_all_your_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=0.94):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_should_return_do_nothing_with_095() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95):
        assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_with_105() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"
