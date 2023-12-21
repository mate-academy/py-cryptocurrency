import pytest
from unittest.mock import patch
from typing import Callable

from app.main import cryptocurrency_action


# Mock the get_exchange_rate_prediction function
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Callable
) -> None:
    # Test when the predicted rate is more than 5% higher
    mock_get_exchange_rate_prediction.return_value = 1.06  # 6% higher
    result = cryptocurrency_action(current_rate=1.0)
    assert result == "Buy more cryptocurrency"

    # Test when the predicted rate is more than 5% lower
    mock_get_exchange_rate_prediction.return_value = 0.94  # 6% lower
    result = cryptocurrency_action(current_rate=1.0)
    assert result == "Sell all your cryptocurrency"

    # Test when the predicted rate is within the 5% difference
    mock_get_exchange_rate_prediction.return_value = 1.03  # 3% higher
    result = cryptocurrency_action(current_rate=1.0)
    assert result == "Do nothing"

    # Test when the predicted rate is more than 5% lower
    mock_get_exchange_rate_prediction.return_value = 0.95  # 6% lower
    result = cryptocurrency_action(current_rate=1.0)
    assert result == "Do nothing"

    # Test when the predicted rate is more than 5% lower
    mock_get_exchange_rate_prediction.return_value = 1.05  # 6% lower
    result = cryptocurrency_action(current_rate=1.0)
    assert result == "Do nothing"


if __name__ == "__main__":
    pytest.main()
