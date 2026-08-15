from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy(mock_pred: Mock) -> None:
    mock_pred.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_pred: Mock) -> None:
    mock_pred.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_pred: Mock) -> None:
    mock_pred.return_value = 80
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_not_sell_at_0_95(mock_pred: Mock) -> None:
    mock_pred.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_not_buy_at_1_05(mock_pred: Mock) -> None:
    mock_pred.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
