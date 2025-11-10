from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 200
    result = cryptocurrency_action(current_rate=100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 50
    result = cryptocurrency_action(current_rate=100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    result = cryptocurrency_action(current_rate=100)
    assert result == "Do nothing"
