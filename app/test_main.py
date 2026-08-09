from typing import Callable
from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 106, "Buy more cryptocurrency"),  # 6% higher
    (100, 94, "Sell all your cryptocurrency"),  # 6% lower
    (100, 103, "Do nothing"),  # 3% higher
    (100, 105, "Do nothing"),  # 5% higher
    (100, 95, "Do nothing"),  # 5% higher
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Callable,
        current_rate: int,
        predicted_rate: int,
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
