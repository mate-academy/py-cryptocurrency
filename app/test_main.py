from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.10

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 0.90

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"
