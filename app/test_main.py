import pytest
from typing import Union
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mock_rate_prediction, expected",
    [
        (100, 150.1, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing")
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        mock_rate_prediction: Union[int, float],
        expected: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = mock_rate_prediction
    result: str = cryptocurrency_action(current_rate)

    assert result == expected
