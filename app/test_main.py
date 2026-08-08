from app.main import cryptocurrency_action
from unittest import mock


def test_buy_more_cryptocurrency_() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency_() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_with_cryptocurrency_() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=102):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_at_exact_105() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_at_exact_95() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
