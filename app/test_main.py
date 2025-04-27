from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.side_effect = lambda exchange_rate: 106.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.side_effect = lambda exchange_rate: 94.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.side_effect = lambda exchange_rate: 102.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_buy(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.side_effect = lambda exchange_rate: 105.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_sell(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.side_effect = lambda exchange_rate: 95.0
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
