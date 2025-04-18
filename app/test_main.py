import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "value, result",
    [
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency")
    ],
    ids=[
        "Prediction -6% -> Sell",
        "Prediction -5% -> Do nothing",
        "Prediction = current -> Do nothing",
        "Prediction +5% -> Do nothing",
        "Prediction +6% -> Buy"
    ]
)
def test_cryptocurrency_action(value: int | float, result: str) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=value
    ):
        assert cryptocurrency_action(1) == result
