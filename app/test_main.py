import pytest

from app.main import cryptocurrency_action
from typing import Union
from unittest.mock import patch


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        predicted_rate: float,
        expected_action: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction = mocked_prediction
        mocked_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == expected_action
        mocked_prediction.assert_called_once_with(current_rate)
