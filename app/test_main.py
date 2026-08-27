from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        pytest.param(1.0, 1.06, "Buy more cryptocurrency",
                     id="buy if more 1.05"),
        pytest.param(1.0, 1.05, "Do nothing",
                     id="shouldn't buy if eq 1.05"),
        pytest.param(1.0, 0.94, "Sell all your cryptocurrency",
                     id="sell if less 0.95"),
        pytest.param(1.0, 0.95, "Do nothing",
                     id="shouldn't sell if eq 0.95"),
        pytest.param(1, 1, "Do nothing",
                     id="do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock.Mock,
        current_rate: int | float,
        predicted_rate: int | float,
        expected: int | float
) -> None:
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
