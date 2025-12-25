import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),

        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),

        (100, 104.9, "Do nothing"),
        (100, 95.1, "Do nothing"),
        (100, 100, "Do nothing"),

        (50, 51, "Do nothing"),
        (200, 198, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_boundary_conditions(
    mock_get_rate: float,
    current_rate: float,
    predicted_rate: float,
    expected_action: float
) -> None:
    mock_get_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
