from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch('app.main.get_exchange_rate_prediction')
def test_buy_more_cryptocurrency(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 1.1  # 10% increase
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"

@patch('app.main.get_exchange_rate_prediction')
def test_sell_all_cryptocurrency(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 0.9  # 10% decrease
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"

@patch('app.main.get_exchange_rate_prediction')
def test_do_nothing_when_small_difference(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 1.05  # 4% increase
    assert cryptocurrency_action(1.0) == "Do nothing"
    mock_get_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"