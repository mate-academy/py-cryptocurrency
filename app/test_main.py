import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_value",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_func,
        current_rate,
        prediction_rate,
        expected_value
):
    mocked_func.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_value
