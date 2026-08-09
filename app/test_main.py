import unittest
from unittest.mock import patch
from app import main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_over_5_percent(mock_pred: unittest.mock.Mock) -> None:
    mock_pred.return_value = 105.01
    result = main.cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_under_5_percent(mock_pred: unittest.mock.Mock) -> None:
    mock_pred.return_value = 94.99
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_pred: unittest.mock.Mock) -> None:
    mock_pred.return_value = 102
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_upper_margin(mock_pred: unittest.mock.Mock) -> None:
    mock_pred.return_value = 105.0
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_margin(mock_pred: unittest.mock.Mock) -> None:
    mock_pred.return_value = 95.0
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"
