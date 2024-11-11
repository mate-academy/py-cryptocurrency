import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.06, 1.0, "Sell all your cryptocurrency"),
        (1.06, 1.06, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ]
)
def test_buy_cryptocurrency(current_rate: Union[int, float],
                            prediction_rate: Union[int, float],
                            expected_result: str) -> None:

    with (mock.patch("app.main_get_exchange_rate_prediction")
          as mock_exchange_rate):
        mock_exchange_rate.return_value = prediction_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
