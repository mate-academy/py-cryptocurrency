from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 107, "Buy more cryptocurrency"),
        (50, 53, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 93, "Sell all your cryptocurrency"),
        (50, 46, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        prediction_rate: int,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected
