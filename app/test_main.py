import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        pytest.param(
            10, 10 * 1.6, "Buy more cryptocurrency",
            id="more than 5% higher"
        ),
        pytest.param(
            10, 10 * 0.94, "Sell all your cryptocurrency",
            id="more than 5% lower"
        ),
        pytest.param(10, 10 * 1.05, "Do nothing", id="difference within 5%"),
        pytest.param(10, 10 * 0.95, "Do nothing", id="difference within 5%"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
        predicted_rate: float,
        expected_action: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        action = cryptocurrency_action(current_rate)
        assert (
            action == expected_action
        ), f"Expected {expected_action}, but got {action}"
