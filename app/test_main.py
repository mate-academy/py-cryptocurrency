from unittest import mock
from typing import Callable
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction_func_been_called(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 11.7
    cryptocurrency_action(10)
    mocked_prediction.assert_called_once_with(10)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto_signal(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 12
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_crypto_signal(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 5
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_high_edge_case_do_nothing_signal(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_low_edge_case_do_nothing_signal(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
