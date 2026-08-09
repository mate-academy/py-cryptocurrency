import pytest

from typing import Callable, Union
from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate,action",
    [
        (112.5, "Buy more cryptocurrency"),
        (105.1, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100.32, "Do nothing"),
        (95, "Do nothing"),
        (94.9, "Sell all your cryptocurrency"),
        (58, "Sell all your cryptocurrency")
    ],
    ids=[
        "buy more cryptocurrency if exchange rate is 5%+ higher",
        "buy more cryptocurrency if exchange rate is 5%+ higher",
        "do nothing if difference is <5%",
        "do nothing if difference is <5%",
        "do nothing if difference is <5%",
        "sell all cryptocurrency if exchange rate is 5%+ lower",
        "sell all cryptocurrency if exchange rate is 5%+ lower",
    ]
)
def test_cryptocurrency_action(
    get_exchange_rate_prediction: Callable,
    prediction_rate: Union[int, float],
    action: str
) -> None:

    get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(100) == action
