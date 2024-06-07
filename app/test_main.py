import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,get_exchange_rate_prediction_return_value, result",
    [
        (10, 10, "Do nothing"),
        (10, 7, "Sell all your cryptocurrency"),
        (10, 13, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.Mock,
        current_rate: float | int,
        get_exchange_rate_prediction_return_value: float | int,
        result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = (
        get_exchange_rate_prediction_return_value)
    assert cryptocurrency_action(current_rate) == result
