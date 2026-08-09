import pytest
from unittest.mock import patch
import app.main


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    # predicted > 5% higher → Buy
    (100, 106.0, "Buy more cryptocurrency"),  # exactly 6% higher
    (100, 200.0, "Buy more cryptocurrency"),  # way higher
    (200, 212.0, "Buy more cryptocurrency"),  # 6% higher, different base

    # predicted > 5% lower → Sell
    (100, 94.0, "Sell all your cryptocurrency"),  # exactly 6% lower
    (100, 50.0, "Sell all your cryptocurrency"),  # way lower
    (200, 188.0, "Sell all your cryptocurrency"),  # 6% lower, different base

    # within 5% range → Do nothing
    (100, 105.0, "Do nothing"),  # exactly 5% higher (not more than 5%)
    (100, 95.0, "Do nothing"),  # exactly 5% lower (not more than 5%)
    (100, 100.0, "Do nothing"),  # no change
    (100, 102.0, "Do nothing"),  # slightly higher but within range
])
def test_cryptocurrency_action(
        current_rate: float, predicted_rate: float, expected: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        assert app.main.cryptocurrency_action(current_rate) == expected
