from unittest.mock import patch
import app.main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: int) -> None:
    mock_prediction.return_value = 106.0
    result = app.main.cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: int) -> None:
    mock_prediction.return_value = 94.0
    result = app.main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_between(mock_prediction: int) -> None:
    mock_prediction.return_value = 97.0
    result = app.main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exactly_95(mock_prediction: int) -> None:
    mock_prediction.return_value = 95.0
    result = app.main.cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exactly_105(mock_prediction: int) -> None:
    mock_prediction.return_value = 105.0
    result = app.main.cryptocurrency_action(100)
    assert result == "Do nothing"
