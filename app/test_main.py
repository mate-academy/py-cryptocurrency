from unittest import mock

import pytest

from app.main import cryptocurrency_action

from typing import Callable


@pytest.mark.parametrize(
    ("current_rate_mark", "prediction_rate", "expected_result"),
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: Callable,
        current_rate_mark: int | float,
        prediction_rate: int | float,
        expected_result: str
) -> None:
    mock_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate_mark)
    assert result == expected_result
