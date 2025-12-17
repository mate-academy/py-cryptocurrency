import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency", id="Above_plus_5_percent"
        ),
        pytest.param(100, 105, "Do nothing", id="Equal_plus_5_percent"),
        pytest.param(100, 100, "Do nothing", id="Equal_current_rate"),
        pytest.param(100, 95, "Do nothing", id="Equal_minus_5_percent"),
        pytest.param(
            100, 94, "Sell all your cryptocurrency", id="Below_plus_5_percent"
        ),
    ],
)
def test_cryptocurrency_action(
    current_rate: int, prediction_rate: int, expected: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected
