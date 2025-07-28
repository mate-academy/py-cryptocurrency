from typing import Union
from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_advice",
    [
        (10, 11, "Buy more cryptocurrency"),
        (12.5, 17, "Buy more cryptocurrency"),
        (13.5, 11, "Sell all your cryptocurrency"),
        (11, 10, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing"),
        (1.1, 1.1, "Do nothing"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_cryptocurrency_action(
        mock_get_prediction_rate: mock.MagicMock,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected_advice: str) -> None:
    mock_get_prediction_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_advice
