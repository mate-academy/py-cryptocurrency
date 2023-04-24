from unittest import mock

import app
from app.main import cryptocurrency_action, get_exchange_rate_prediction


def test_function_was_called() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 1
        cryptocurrency_action(1)
        mocked_func.assert_called_once_with(1)


def test_function_should_return_buy_more_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 2
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_function_should_return_sell_all_your_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 0.5
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_function_should_return_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 1.04
        assert cryptocurrency_action(1) == "Do nothing"
