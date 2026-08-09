from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "mocked_prediction_return, rate, expected",
    [
        (
            1.75, 1.50, "Buy more cryptocurrency"
        ),
        (
            1.50, 2.01, "Sell all your cryptocurrency"
        ),
        (
            2.01, 2.01, "Do nothing"
        ),
        (
            2.10, 2.00, "Do nothing"
        ),
        (
            1.90, 2.00, "Do nothing"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_rate_prediction: any,
    mocked_prediction_return: float,
    rate: float,
    expected: str
) -> None:
    mocked_rate_prediction.return_value = mocked_prediction_return
    assert cryptocurrency_action(rate) == expected
