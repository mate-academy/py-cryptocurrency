from collections.abc import Callable
from unittest import mock

from app.main import cryptocurrency_action


def test_get_exchange_rate_prediction_called() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 0.1
        cryptocurrency_action(3.5)
        mock_predict.assert_called_once_with(3.5)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_buy(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 9.71
    assert (
        cryptocurrency_action(20) == "Sell all your cryptocurrency"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_sell(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 0.45
    assert (
        cryptocurrency_action(20) == "Sell all your cryptocurrency"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_do_nothing_95(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 95
    assert (
        cryptocurrency_action(100) == "Do nothing"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_do_nothing_105(mocked_prediction: Callable) -> None:
    mocked_prediction.return_value = 105
    assert (
        cryptocurrency_action(100) == "Do nothing"
    )
