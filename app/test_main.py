from typing import Any

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,message",
    [
        (106, 100, "Buy more cryptocurrency"),
        (101, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ],
    ids=[
        "more than 5% higher from the current",
        "between 5% higher and 5% lower",
        "more than 5% lower",
        "5% higher",
        "5% lower"
    ]

)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: Any,
        prediction_rate: int,
        current_rate: int,
        message: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == message
