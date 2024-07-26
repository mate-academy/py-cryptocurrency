import pytest
from unittest.mock import patch, Mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_result, result",
    [
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (54.3, 51.580, "Sell all your cryptocurrency"),
        (61.8, 64.90, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: Mock,
        current_rate: Union[int, float],
        prediction_result: Union[int, float],
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_result

    assert cryptocurrency_action(current_rate) == result

    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)
