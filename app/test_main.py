import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected_action: str,
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected_action
