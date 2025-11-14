# write your code here
import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),  # >5% increase
        (100, 95, "Do nothing"),               # exactly 5% down → do nothing
        (100, 94, "Sell all your cryptocurrency"),  # >5% decrease
        (100, 104.99, "Do nothing"),           # just below 5% up → do nothing
        (100, 105, "Do nothing"),              # exactly 5% up → do nothing
    ]
)
def test_cryptocurrency_action(current_rate, predicted_rate, expected):
    """Test all possible actions with mocked prediction."""
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected
