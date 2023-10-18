import pytest
from typing import Any
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (11.44, 13, "Sell all your cryptocurrency"),
        (115.65, 100, "Buy more cryptocurrency"),
        (1.02, 1, "Do nothing"),
        (23.75, 25, "Do nothing"),
        (42, 40, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_function(
        mock_get_exchange_rate_prediction: float,
        prediction_rate: Any,
        current_rate: Any,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
