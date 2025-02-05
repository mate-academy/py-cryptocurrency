from app.main import cryptocurrency_action
from unittest.mock import patch
import pytest
from typing import Union


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 105.01, "Buy more cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 104.99, "Do nothing"),
    (100, 95.01, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 94.99, "Sell all your cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
])
def test_cryptocurrency_action(current_rate: Union[int, float],
                               predicted_rate: Union[int, float],
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expectedgit
