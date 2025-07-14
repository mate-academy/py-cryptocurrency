from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_get_buy(mock_predict: MagicMock) -> None:
    mock_predict.return_value = 9.4
    result = cryptocurrency_action(10)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_get_sell(mock_predict: MagicMock) -> None:
    mock_predict.return_value = 10.6
    result = cryptocurrency_action(10)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_get_nothing(mock_predict: MagicMock) -> None:
    mock_predict.return_value = 9.9
    result = cryptocurrency_action(10)
    assert result == "Do nothing"
