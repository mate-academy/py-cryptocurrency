from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 105
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 90
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 98
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"

    mock_get_prediction.return_value = 102
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_conditions(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 105.01
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"

    mock_get_prediction.return_value = 94.99
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_get_prediction: MagicMock) -> None:
    mock_get_prediction.return_value = 95
    current_rate = 100
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
