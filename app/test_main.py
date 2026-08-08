import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, rate_prediction, action",
    [
        (10, 11, "Buy more cryptocurrency"),
        (10, 124, "Buy more cryptocurrency"),
        (1, 1.06, "Buy more cryptocurrency"),
        (10, 9, "Sell all your cryptocurrency"),
        (100, 23, "Sell all your cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.98, "Do nothing"),
        (1, 1.02, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        rate_prediction: int | float,
        current_rate: int | float,
        action: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=rate_prediction
    ):
        assert cryptocurrency_action(current_rate) == action
