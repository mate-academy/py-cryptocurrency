import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, expected_result",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 85, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        predict_rate: int | float,
        expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predict_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
