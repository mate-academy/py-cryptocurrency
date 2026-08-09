from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_more_then_5_percent(mock_exchange_rate: any) -> None:
    mock_exchange_rate.return_value = 105.1
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_lower_then_5_percent(mock_exchange_rate: any) -> None:
    mock_exchange_rate.return_value = 94.9
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_different(mock_exchange_rate: any) -> None:
    mock_exchange_rate.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_different_with_low_predict_value(
        mock_exchange_rate: any
) -> None:
    mock_exchange_rate.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
