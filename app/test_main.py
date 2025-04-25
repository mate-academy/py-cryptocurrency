from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: int) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 106.0  # > 5% increase
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: int) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 94.0  # > 5% decrease
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: int) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 97.0  # within ±5%
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
