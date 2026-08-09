import app.main as main
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_buy1(mock_pred: int) -> str:
    mock_pred.return_value = 110
    result = main.cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_at_105_percent_boundary(mock_pred: int) -> str:
    mock_pred.return_value = 105.01
    result = main.cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_105_should_be_do_nothing(mock_pred: int) -> str:
    mock_pred.return_value = 105.0
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy3(mock_pred: int) -> str:
    mock_pred.return_value = 100
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_95_should_be_do_nothing(mock_pred: int) -> str:
    mock_pred.return_value = 95
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_at_94_percent_boundary(mock_pred: int) -> str:
    mock_pred.return_value = 94
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy5(mock_pred: int) -> str:
    mock_pred.return_value = 90
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy6(mock_pred: int) -> str:
    mock_pred.return_value = 85
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_buy7(mock_pred: int) -> str:
    mock_pred.return_value = 80
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
