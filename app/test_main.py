import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected",
    [
        (105.01, "Buy more cryptocurrency"),
        (94.99, "Sell all your cryptocurrency"),
        (100.0, "Do nothing"),
        (104.99, "Do nothing"),
        (95.1, "Do nothing"),
        (105.0, "Do nothing"),
        (95.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(predicted_rate: float, expected: str) -> None:
    currency_rate = 100.0
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        assert cryptocurrency_action(currency_rate) == expected
