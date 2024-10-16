from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate, predication_rate, action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 98, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ],
    ids=[
        "buy more cryptocurrency",
        "sell all your cryptocurrency",
        "do nothing",
        "do nothing",
        "do nothing"
    ]
)
def test_cryptocurrency_action(
    predication_rate: int | float,
    current_rate: int | float,
    action: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = predication_rate
        assert cryptocurrency_action(current_rate) == action
