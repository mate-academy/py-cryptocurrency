from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_higher(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_lower(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_within_change(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"
    mock_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
