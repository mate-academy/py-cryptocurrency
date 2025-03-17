import pytest

from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: float,
        expected_action: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_action
