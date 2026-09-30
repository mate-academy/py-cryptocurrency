from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_prediction_is_5_percent_higher(mock_pred: Mock) -> None:
    mock_pred.return_value = 106  # Exemplo: 5% acima de 100
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_prediction_is_5_percent_lower(mock_pred: Mock) -> None:
    mock_pred.return_value = 94  # Exemplo: 5% abaixo de 100
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_prediction_limit_lower(mock_pred: Mock) -> None:
    mock_pred.return_value = 95  # em 5% abaixo
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_prediction_limit_higher(mock_pred: Mock) -> None:
    mock_pred.return_value = 105  # em 5% acima
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
