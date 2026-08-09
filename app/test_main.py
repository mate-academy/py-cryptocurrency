import pytest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, mock_prediction, expected", [
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
])
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        mock_prediction: float,
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=mock_prediction
    ):
        result: str = cryptocurrency_action(current_rate)
        assert result == expected
