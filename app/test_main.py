# write your code here

from app.main import cryptocurrency_action
import pytest
from typing import Union
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction, current_rate, outcome",
    [
        (11.44, 13, "Sell all your cryptocurrency"),
        (115.65, 100, "Buy more cryptocurrency"),
        (1.02, 1, "Do nothing"),
        (23.75, 25, "Do nothing"),
        (42, 40, "Do nothing")
    ]
)
def test_if_got_right_exchange_rate_prediction(
    mocked_exchange_rate_prediction: float,
    prediction: float,
    current_rate: Union[float, int],
    outcome: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == outcome
