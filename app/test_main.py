from unittest.mock import patch
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted, expected",
    [
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 94.0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(current_rate: int,
                               predicted: float,
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted):
        assert cryptocurrency_action(current_rate) == expected
