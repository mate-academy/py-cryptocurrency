from unittest import mock

from app.main import cryptocurrency_action


def test_function_was_called() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 1
        cryptocurrency_action(1)
        mocked_func.assert_called_once_with(1)


def test_function_should_return_buy_more_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 1.06
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_function_should_return_sell_all_your_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 0.94
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_function_should_return_do_nothing_max_value() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"


def test_function_should_return_do_nothing_min_value() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
