from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_higher_than_five_percent(
        mock_get_exchange_rate_prediction: mock.Mock) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 106
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_lower_than_five_percent(
        mock_get_exchange_rate_prediction: mock.Mock) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_within_five_percent(
        mock_get_exchange_rate_prediction: mock.Mock) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)
