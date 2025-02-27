import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ]
)
def test_control_signals_for_buy_and_sell(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected
