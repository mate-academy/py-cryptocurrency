import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected",
    [
        pytest.param(0.5, "Buy more cryptocurrency",
                     id="when to buy"),
        pytest.param(1.05, "Do nothing",
                     id="when there is nothing to do"),
        pytest.param(2, "Sell all your cryptocurrency",
                     id="when to sell")
    ]
)
def test_cryptocurrency_action(
        current_rate: (int | float),
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.95):
        assert cryptocurrency_action(current_rate) == expected
