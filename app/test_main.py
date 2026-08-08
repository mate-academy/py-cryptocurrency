from typing import Union

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected", [
        pytest.param(100, 106, "Buy more cryptocurrency",
                     id="Forecast is more than 5% higher"),
        pytest.param(100, 94, "Sell all your cryptocurrency",
                     id="Forecast is more than 5% lower"),
        pytest.param(100, 100, "Do nothing",
                     id="No change"),
        pytest.param(100, 105, "Do nothing",
                     id="Forecast is exactly 5% higher"),
        pytest.param(100, 95, "Do nothing",
                     id="Forecast is exactly 5% lower"),
        pytest.param(100, 97, "Do nothing",
                     id="Forecast within ±5%")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: Union[int, float],
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected: str
) -> None:
    mock_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
