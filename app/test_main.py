import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "exchange_rate, expected_response",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
    ],
    ids=[
        "Exchange rate more than 5% higher",
        "Exchange rate more than 5% lower",
        "Low difference",
        "Max acceptable difference",
        "Min acceptable difference",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock,
        exchange_rate: float,
        expected_response: str,
) -> None:
    mocked_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(1) == expected_response
