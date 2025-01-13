from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_prediction: int) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 106
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_get_prediction: int) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 94
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_prediction: int) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 101
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_min(mock_get_prediction: int) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_max(mock_get_prediction: int) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
