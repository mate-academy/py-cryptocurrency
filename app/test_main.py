from unittest.mock import patch
from typing import Any
import app.main as main


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange_rate_prediction: Any) -> None:
    main.get_exchange_rate_prediction = mock_exchange_rate_prediction

    mock_exchange_rate_prediction.return_value = 1.07 * 100  # 7% increase
    result = main.cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"

    mock_exchange_rate_prediction.return_value = 0.92 * 100  # 8% decrease
    result = main.cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"

    mock_exchange_rate_prediction.return_value = 0.98 * 100  # 2% decrease
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"

    mock_exchange_rate_prediction.return_value = 100  # Same rate
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing"
