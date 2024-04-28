from __future__ import annotations
import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ],
    ids=["predicted exchange rate is more than 5% higher from the current",
         "predicted exchange rate is more than 5% lower from the current",
         "difference is lower than 5%",
         "difference is lower than 5%"
         ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock,
        prediction_rate: int | float,
        current_rate: int | float,
        result: str
) -> None:
    mocked_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == result
