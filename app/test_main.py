import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(2, 1, "Sell all your cryptocurrency",
                     id="sell, when quotient < 0.95"),
        pytest.param(1, 1.05, "Do nothing",
                     id="stay, when quotient == 1.05"),
        pytest.param(1, 0.95, "Do nothing",
                     id="stay, when quotient == 0.95"),
        pytest.param(96, 100, "Do nothing",
                     id="stay, when 0.95 < quotient > 1.05"),
        pytest.param(18, 20, "Buy more cryptocurrency",
                     id="buy, when quotient > 1.05"),
    ]
)
def test_cryptocurrency_action(
        current_rate: (int | float),
        prediction_rate: (int | float),
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected
