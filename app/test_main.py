import pytest
from unittest.mock import MagicMock, patch
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_action",
    [
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
    ],
)
@patch("main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    predicted_rate: Union[int, float],
    current_rate: Union[int, float],
    expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
