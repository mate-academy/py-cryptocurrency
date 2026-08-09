import pytest
from typing import Union
from unittest import mock

from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        pytest.param(
            1, 1.05, "Do nothing",
            id="prediction rate = current rate * 1.05"),
        pytest.param(
            1, 1.06, "Buy more cryptocurrency",
            id="prediction rate = current rate * 1.06"),
        pytest.param(
            1, 0.94, "Sell all your cryptocurrency",
            id="prediction rate = current rate * 0.94"),
        pytest.param(
            1, 0.95, "Do nothing",
            id="prediction rate = current rate * 0.95")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
