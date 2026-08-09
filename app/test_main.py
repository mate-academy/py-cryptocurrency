from unittest.mock import patch, MagicMock
from typing import Union
import pytest


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, prediction_result",
    [
        pytest.param(
            1.01,
            1,
            "Do nothing",
            id="Do nothing when rate = 1"),
        pytest.param(
            1.00,
            1.05,
            "Do nothing",
            id="Do nothing when rate = 1.05"),
        pytest.param(
            1.00,
            1.06,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency when rate = 1.06"),
        pytest.param(
            1.00,
            0.94,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency when rate = 0.94"),
        pytest.param(
            1.00,
            0.95,
            "Do nothing",
            id="Do nothing when rate = 0.95"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        exchange_rate: float,
        prediction_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == prediction_result
