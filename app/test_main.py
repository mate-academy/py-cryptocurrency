from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float
) -> None:
    mock_get_exchange_rate_prediction.return_value = 110.0

    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 90.0

    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"

    mock_get_exchange_rate_prediction.return_value = 105.0

    assert cryptocurrency_action(100.0) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 95.0

    assert cryptocurrency_action(100.0) == "Do nothing"
