from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy_action(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell_action(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_inside_bounds(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 98
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
