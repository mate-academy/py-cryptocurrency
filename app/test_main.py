from unittest import mock

from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=10.6
    ):
        assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=9.4
    ):
        assert cryptocurrency_action(10.0) == "Sell all your cryptocurrency"


def test_do_nothing_with_max_limit() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=9.5
    ):
        assert cryptocurrency_action(10) == "Do nothing"


def test_do_nothing_with_min_limit() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=10.5
    ):
        assert cryptocurrency_action(10) == "Do nothing"
