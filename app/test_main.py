from typing import Callable
from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: Callable) -> None:
    mock_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    mock_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    mock_prediction.return_value = 1.03
    assert cryptocurrency_action(1) == "Do nothing"

    mock_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"

    mock_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
