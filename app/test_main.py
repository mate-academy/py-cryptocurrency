from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_cryptocurrency(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 100
    result = cryptocurrency_action(103)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_boundary(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_boundary(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
