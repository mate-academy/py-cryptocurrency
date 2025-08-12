import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,current_rate,expected",
    [
        (105.1, 100, "Buy more cryptocurrency"),
        (94.9, 100, "Sell all your cryptocurrency"),
        (102, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        predicted_rate: int | float,
        current_rate: int | float,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected
