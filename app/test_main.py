from app.main import cryptocurrency_action
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_if_crypto_grows(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_crypto_falls(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_crypto_less_but_still(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_if_crypto_bigger_but_still(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
