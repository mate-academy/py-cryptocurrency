from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,expected_response",
    [
        (10.6, "Buy more cryptocurrency"),
        (9.4, "Sell all your cryptocurrency"),
        (10, "Do nothing"),
        (9.5, "Do nothing"),
        (10.5, "Do nothing")
    ],
    ids=[
        "Exchange rate is more than 5% higher",
        "Exchange rate is more than 5% lower",
        "Difference is not that much",
        "Min limit exchange rate, with little difference",
        "Max limit exchange rate, with little difference"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock,
        exchange_rate: float,
        expected_response: str
) -> None:
    mocked_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(10) == expected_response
