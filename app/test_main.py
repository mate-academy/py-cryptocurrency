from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        [100.1, 120, "Buy more cryptocurrency"],
        [100.1, 90, "Sell all your cryptocurrency"],
        [100, 105, "Do nothing"],
        [100, 95, "Do nothing"]

    ],
    ids=[
        "You should buy coins when prediction / current rate > 1.05",
        "You should sell coins when prediction / current rate < 0.95",
        "You should not buy coins when prediction / current rate == 1.05",
        "You should not sell coins when prediction / current rate == 0.95",
    ]
)
def test_cryptocurrency_action(
        current_rate: float | int,
        prediction_rate: float | int,
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        mocked_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
