from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Any


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (19, 20, "Do nothing"),
        (21, 20, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_exchange_rate: Any,
    prediction_rate: int,
    current_rate: int,
    expected_result: str,
) -> None:
    mock_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
