# write your code here
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_positive(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 120
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once_with(100)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_negative(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 80
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once_with(100)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_same_value(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 101.12
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_get_exchange_rate_prediction.assert_called_once_with(100)
