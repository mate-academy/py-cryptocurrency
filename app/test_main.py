from unittest import mock

from .main import cryptocurrency_action


def test_function_has_called_not_buy_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mockexcpredict:
        mockexcpredict.return_value = 1.01
        assert cryptocurrency_action(1) == "Do nothing"


def test_function_has_called_buy_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mockexcpredict:
        mockexcpredict.return_value = 1.13
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_function_has_called_sell_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mockexcpredict:
        mockexcpredict.return_value = 0.8
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_function_has_called_not_buy_min_level_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mockexcpredict:
        mockexcpredict.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"


def test_function_has_called_not_buy_max_level_crypto() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mockexcpredict:
        mockexcpredict.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"
