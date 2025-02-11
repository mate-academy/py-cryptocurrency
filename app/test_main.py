from app.main import cryptocurrency_action
from unittest.mock import patch
import pytest


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
    (100, 104.9, "Do nothing"),
    (100, 95.1, "Do nothing"),
    (100, 95.0, "Do nothing"),
    (100, 105.0, "Do nothing"),
])
def test_cryptocurrency_action(current_rate, predicted_rate, expected):
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected
