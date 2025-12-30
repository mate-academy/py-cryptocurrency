from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Any


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        (11, 10, "Buy more cryptocurrency"),
        (9, 10, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing"),
        (9.5, 10, "Do nothing"),
        (10.5, 10, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    get_exchange_rate_prediction: Any,
    prediction_rate: int | float,
    current_rate: int | float,
    expected_result: str,
) -> None:
    get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
