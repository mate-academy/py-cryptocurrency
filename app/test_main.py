import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        (1000, 1060, "Buy more cryptocurrency"),
        (2000, 2100, "Do nothing"),
        (2000, 1900, "Do nothing"),
        (10000, 950, "Sell all your cryptocurrency"),
        (3500, 200, "Sell all your cryptocurrency"),
    ],
    ids=[
        ("Should Buy more cryptocurrency if predicted rate"
         " is more than 5% higher from the current"),
        ("You should not buy cryptocurrency when prediction"
         "rate / current_rate == 1.05"),
        ("You should not sell cryptocurrency when prediction"
         " rate / current_rate == 0.95"),
        ("Should Sell all cryptocurrency if predicted"
         " rate is more than 5% lower from the current"),
        ("Should Sell all cryptocurrency if predicted"
         " rate is more than 5% lower from the current")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        exchange_rate: int,
        expected: str
) -> None:

    def mocked_prediction(*args) -> int | float:
        return exchange_rate

    with mock.patch(
            "app.main.get_exchange_rate_prediction", mocked_prediction
    ):

        assert cryptocurrency_action(current_rate) == expected
