from unittest import mock
from typing import Callable


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(
        mock_get_prediction: Callable
) -> None:
    mock_get_prediction.return_value = 170
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_crypto(
    mock_get_prediction: Callable
) -> None:
    mock_get_prediction.return_value = 90
    result = cryptocurrency_action(150)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
    mock_get_prediction: Callable
) -> None:
    mock_get_prediction.return_value = 101
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(
        mock_get_prediction: Callable
) -> None:
    mock_get_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(
        mock_get_prediction: Callable
) -> None:
    mock_get_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
