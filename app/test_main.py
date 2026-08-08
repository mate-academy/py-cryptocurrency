from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_5_percent_more(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_5_percent_less(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_2_percent_more(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_2_percent_less(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_equal(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
