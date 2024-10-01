import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 150, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: callable,
    current_rate: int | float,
    prediction_rate: int | float,
    result: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
