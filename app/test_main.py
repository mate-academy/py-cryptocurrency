from unittest import mock
from app.main import cryptocurrency_action
from typing import Union
import pytest


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [

        (96, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (104, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency")
    ]
)
def test_get_exchange_rate_prediction(
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction_rate):
        mocked_prediction_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
