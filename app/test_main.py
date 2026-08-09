from unittest.mock import Mock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_predict: "Mock") -> None:
    mock_predict.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_95_percent(mock_predict: Mock) -> None:
    mock_predict.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_105_percent(mock_predict: Mock) -> None:
    mock_predict.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
