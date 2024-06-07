import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(10, 15.0, "Buy more cryptocurrency"),
        pytest.param(15.5, 10, "Sell all your cryptocurrency"),
        pytest.param(15, 15.1, "Do nothing"),
        pytest.param(0, 15, "Do nothing")
    ],
    ids=[
        "Predict higher, buy",
        "Predict lower, sell",
        "Predict similar, hold",
        "Current rate zero"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate: mock.Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str) -> None:
    if current_rate == 0:
        with pytest.raises(ZeroDivisionError):
            cryptocurrency_action(current_rate)
    else:
        mocked_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
