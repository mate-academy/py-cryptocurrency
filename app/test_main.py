from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Union


# Mock function
def mock_get_exchange_rate_prediction() -> None:
    return 0.0  # Placeholder, will be set in tests


# Test cases
@patch("app.main.get_exchange_rate_prediction",
       side_effect=mock_get_exchange_rate_prediction
       )
def test_cryptocurrency_action(mock_get_rate: Union[int, float]) -> str:
    # Test case where predicted rate is more than 5% higher
    mock_get_rate.side_effect = lambda x: 1.10  # 10% higher
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"

    # Test case where predicted rate is more than 5% lower
    mock_get_rate.side_effect = lambda x: 0.90  # 10% lower
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"

    # Test case where predicted rate is within 5% range
    mock_get_rate.side_effect = lambda x: 1.05  # 4% higher
    assert cryptocurrency_action(1.0) == "Do nothing"

    mock_get_rate.side_effect = lambda x: 0.95  # 4% lower
    assert cryptocurrency_action(1.0) == "Do nothing"
