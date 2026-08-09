import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ],
    ids=[
        "buy_more_cryptocurrency",
        "sell_all_cryptocurrency",
        "do_nothing_exactly_105_percent",
        "do_nothing_exactly_95_percent",
        "do_nothing_slightly_higher",
        "do_nothing_slightly_lower"
    ]
)
def test_cryptocurrency_action(current_rate: float,
                               predicted_rate: float,
                               expected_action: str) -> None:
    with (patch("app.main.get_exchange_rate_prediction",
                return_value=predicted_rate)):
        result = cryptocurrency_action(current_rate)
        assert result == expected_action, (
            f"Expected '{expected_action}' "
            f"but got '{result}'")
