from __future__ import annotations
import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.06, 1.06, "Do nothing"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_exchange_rate: mock.Mock,
                               prediction_rate: int | float,
                               current_rate: int | float,
                               result: str) -> None:

    mocked_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
