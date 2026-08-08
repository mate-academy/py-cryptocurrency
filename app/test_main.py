from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
