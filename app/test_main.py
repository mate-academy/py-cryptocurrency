import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action, get_exchange_rate_prediction

@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),      # +6% (більше +5%)
        (100, 94, "Sell all your cryptocurrency"), # -6% (менше -5%)
        (100, 104, "Do nothing"),                   # +4% (менше +5%)
        (100, 96, "Do nothing"),                    # -4% (більше -5%)
        (100, 105, "Do nothing"),                   # +5% (рівно +5%)
        (100, 95, "Do nothing"),                    # -5% (рівно -5%)
    ]
)
def test_cryptocurrency_action(current_rate, predicted_rate, expected_action):
    with patch('app.main.get_exchange_rate_prediction', return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected_action
