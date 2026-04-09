from __future__ import annotations
import pytest
from unittest.mock import MagicMock, patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
    ],
    ids=[
        "increase_more_than_5_percent",
        "decrease_more_than_5_percent",
        "increase_less_than_5_percent",
        "decrease_less_than_5_percent",
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: Union[int | float],
        predicted_rate: Union[int | float],
        expected: str
) -> None:
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected
    mock_prediction.assert_called_once_with(current_rate)
