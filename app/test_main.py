from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    current_rate = 90
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = current_rate * 1.05
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"

@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    current_rate = 90
    mock_get_exchange_rate_prediction.return_value = 84
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = current_rate * 0.95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_get_exchange_rate_prediction: mock.MagicMock) -> None:
    current_rate = 90
    mock_get_exchange_rate_prediction.return_value = 92
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
