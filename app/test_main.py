from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
    ],
    ids=[
        "Buy",
        "Sell",
        "Do nothing (top boundary)",
        "Do nothing (bottom boundary)",
        "Do nothing",
    ]
)
def test_exchange_rate(
        current_rate: float | int,
        predicted_rate: float | int,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) \
            as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected
