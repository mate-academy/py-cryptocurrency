import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, mocked_prediction, expected", [
    (95, 105, "Buy more cryptocurrency"),
    (105, 95, "Sell all your cryptocurrency"),
    (102, 103, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing")
])
def test_cryptocurrency_action(
        current_rate: int | float,
        mocked_prediction: int | float,
        expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=mocked_prediction):
        result = cryptocurrency_action(current_rate)
        assert result == expected
