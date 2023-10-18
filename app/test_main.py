from unittest import mock
from .main import cryptocurrency_action
from typing import Union
import pytest


@pytest.mark.parametrize(
    "current_rate",
    "prediction_rate",
    "expected_result",
    [
        (1000, 1060, "Buy more cryptocurrency"),
        (1000, 900, "Sell all your cryptocurrency"),
        (1000, 1010, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
