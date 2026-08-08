import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        # более 5% рост
        (100, 106, "Buy more cryptocurrency"),
        # ровно 5% рост
        (100, 105, "Do nothing"),
        # более 5% падение
        (100, 94, "Sell all your cryptocurrency"),
        # ровно 5% падение
        (100, 95, "Do nothing"),
        # незначительное изменение
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        predicted_rate: int,
        expected: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected
