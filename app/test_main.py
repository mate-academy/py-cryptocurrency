from unittest import mock
from app.main import cryptocurrency_action

@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
    mock_get_exchange_rate_prediction.return_value = 101
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"