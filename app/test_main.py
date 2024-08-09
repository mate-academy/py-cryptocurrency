from app.main import cryptocurrency_action
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_get_prediction: "MagicMock") -> None:
    current_rate = 100.0
    mock_get_prediction.return_value = 105.0  # Exactly 5% higher
    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_get_prediction: "MagicMock") -> None:
    current_rate = 100.0
    mock_get_prediction.return_value = 95.0  # Exactly 5% lower
    assert cryptocurrency_action(current_rate) == "Do nothing"
