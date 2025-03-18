from unittest.mock import patch

from app.main import cryptocurrency_action

@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 2

    result = cryptocurrency_action(mock_get_exchange_rate_prediction)

    assert result == "Buy more cryptocurrency"
    assert result == "Sell all your cryptocurrency"
    assert result == "Do nothing"