import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105.1 , "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 108, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing")
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               predicted_rate: int | float,
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected
