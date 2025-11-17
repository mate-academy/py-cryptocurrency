import pytest
from unittest import mock
from unittest.mock import Mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Mock,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)
