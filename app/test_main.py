from pytest import mark
from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (500, 476, "Buy more cryptocurrency"),
        (470, 500, "Sell all your cryptocurrency"),
        (500, 500, "Do nothing"),
        (525, 500, "Do nothing"),
        (475, 500, "Do nothing")
    ]
)
def test_function_gets_boundary_values(
        prediction_rate: float,
        current_rate: Union[int, float],
        result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_rate_prediction):
        mocked_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
