from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 106
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 94
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_within_threshold(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 97
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_exactly_95_percent(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_exactly_105_percent(mock_prediction: Mock) -> None:
    current_rate = 100
    mock_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
