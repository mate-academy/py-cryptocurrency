import pytest
from typing import Union
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 90, "Sell all your cryptocurrency")
    ]
)
def test_if_should_buy_more(
    current_rate: Union[int, float],
    prediction_rate: int,
    expected_result: str
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_result
