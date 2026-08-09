from unittest.mock import patch
import pytest
from app import main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ],
    ids=[
        "up > 5% case 1",
        "up > 5% case 2",
        "down > 5% case 1",
        "down > 5% case 2",
        "up exactly 5%",
        "down exactly 5%",
        "up < 5%",
        "down < 5%",
    ]
)
def test_cryptocurrency_action_various_scenarios(
        current_rate: int,
        predicted_rate: int,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        result = main.cryptocurrency_action(current_rate)
        assert result == expected
