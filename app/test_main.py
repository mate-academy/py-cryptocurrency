from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 98, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ],
    ids=[
        "increase_above_5_percent",
        "decrease_below_5_percent",
        "no_significant_change",
        "increase_not_significant_change",
        "decrease_not_significant_change"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: patch,
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    """
    Test cryptocurrency_action function based on predicted exchange rates.

    Parameters:
    - current_rate (float): Current exchange rate.
    - predicted_rate (float): Predicted exchange rate.
    - expected_action (str): Expected action based on the predicted rate.
    """
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    action = cryptocurrency_action(current_rate)
    assert action == expected_action, (f"Expected action {expected_action}, "
                                       f"but got {action}")
