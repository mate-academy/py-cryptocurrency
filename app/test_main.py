from typing import Union, Callable
from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction,current_rate,result",
    [
        (1.1, 1, "Buy more cryptocurrency"),
        (0.85, 1, "Sell all your cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
    ],
    ids=[
        "if prediction/current: 1.1 / 0.85, should return buy",
        "if prediction/current: 0.85 / 1.07, should return sell",
        "if prediction/current: 0.95 / 1, should return nothing",
        "if prediction/current: 1.05 / 1, should return nothing"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction: Callable,
                               current_rate: Union[int, float],
                               result: str,
                               prediction: Union[int, float]) -> None:

    mocked_prediction.return_value = prediction

    assert cryptocurrency_action(current_rate) == result
