from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy(mock_func: MagicMock) -> None:
    mock_func.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_func: MagicMock) -> None:
    mock_func.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_to_do_nothing(mock_func: MagicMock) -> None:
    mock_func.return_value = 104
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_buy(mock_func: MagicMock) -> None:
    mock_func.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_sell(mock_func: MagicMock) -> None:
    mock_func.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
