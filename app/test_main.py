import pytest
from unittest.mock import patch
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mocked_prediction_rate, current_rate, expected_action",
    [
        pytest.param(10.5, 10, "Buy more cryptocurrency"),
        pytest.param(9.0, 10, "Sell all your cryptocurrency"),
        pytest.param(10.3, 10, "Do nothing"),
        pytest.param(11.025, 10.5, "Do nothing"),
    ],
    ids=[
        "exchange_rate > 5% higher",
        "exchange_rate > 5% lower",
        "exchange_rate is within ±5%",
        "exchange_rate is 5%"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: patch,
        mocked_prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_action: str,
):
    mock_get_exchange_rate_prediction.return_value = mocked_prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
