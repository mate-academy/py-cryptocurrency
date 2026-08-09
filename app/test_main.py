from app.main import cryptocurrency_action
from unittest.mock import patch, Mock


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 106
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 90
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
