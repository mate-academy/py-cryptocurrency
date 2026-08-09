import pytest

from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (10, 12, "Buy more cryptocurrency"),
        (10, 10.6, "Buy more cryptocurrency"),
        (10, 10.5, "Do nothing"),
        (10, 10, "Do nothing"),
        (10, 9.5, "Do nothing"),
        (10, 9.4, "Sell all your cryptocurrency"),
        (10, 8, "Sell all your cryptocurrency"),
    ]
)
def test_should_check_cryptocurrency_prediction(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_result
