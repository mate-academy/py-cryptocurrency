from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_is_prediction_function_called(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 1.1
    cryptocurrency_action(1.1)
    mocked_get_rate_prediction.assert_called_once_with(1.1)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_buy_more(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 1.2
    result = cryptocurrency_action(1.05)
    assert (
        result == "Buy more cryptocurrency"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_with_prediction_rate_1_05(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1.0)
    assert (
        result == "Do nothing"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_sell_all(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 0.8
    result = cryptocurrency_action(1.2)
    assert (
        result == "Sell all your cryptocurrency"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_do_nothing(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 1.0
    result = cryptocurrency_action(1.0)
    assert (
        result == "Do nothing"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_with_prediction_rate_0_95(
        mocked_get_rate_prediction: Any
) -> None:
    mocked_get_rate_prediction.return_value = 0.95
    result = cryptocurrency_action(1.0)
    assert (
        result == "Do nothing"
    )
