from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@mock.patch('app.main.get_exchange_rate_prediction')
def test_get_exchange_rate_prediction_do_nothing_upper(
        mock_get_exchange_rate_prediction: Any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 2.1
    result = cryptocurrency_action(2)
    mock_get_exchange_rate_prediction.assert_called_once_with(2)
    assert result == "Do nothing"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_get_exchange_rate_prediction_do_nothing_lower(
        mock_get_exchange_rate_prediction: Any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.9
    result = cryptocurrency_action(2)
    mock_get_exchange_rate_prediction.assert_called_once_with(2)
    assert result == "Do nothing"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_get_exchange_rate_prediction_sell(
        mock_get_exchange_rate_prediction: Any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.8
    result = cryptocurrency_action(2)
    mock_get_exchange_rate_prediction.assert_called_once_with(2)
    assert result == "Sell all your cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction')
def test_get_exchange_rate_prediction_buy(
        mock_get_exchange_rate_prediction: Any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 2.2
    result = cryptocurrency_action(2)
    mock_get_exchange_rate_prediction.assert_called_once_with(2)
    assert result == "Buy more cryptocurrency"
