from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_higher_than_five_percent(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_lower_than_five_percent(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    mock_get_exchange_rate_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_is_five_percent_higher(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_exchange_rate_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_exchange_rate_is_five_percent_lower(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_exchange_rate_prediction.assert_called_once()
