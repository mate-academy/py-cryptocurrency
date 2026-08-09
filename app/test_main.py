import unittest.mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 110, "Buy more cryptocurrency"),
        (95, 90, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate: int,
    predicted_rate: int,
    expected: str
) -> None:
    with unittest.mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected
