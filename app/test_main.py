from typing import Callable
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.2
    result = cryptocurrency_action(1)

    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.8
    result = cryptocurrency_action(1)

    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_2(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    result = cryptocurrency_action(1)

    assert result == "Do nothing"
