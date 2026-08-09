from collections.abc import Callable
import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (
            1,
            1.06,
            "Buy more cryptocurrency"
        ),
        (
            1,
            0.94,
            "Sell all your cryptocurrency"
        ),
        (
            1,
            1.05,
            "Do nothing"
        ),
        (
            1,
            0.95,
            "Do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_prediction: Callable,
        current_rate: int,
        prediction_rate: float,
        expected: str) -> None:
    mock_get_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
    mock_get_prediction.assert_called_once_with(current_rate)
