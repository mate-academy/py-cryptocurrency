from typing import Union
from unittest import mock

import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate_prediction, result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_prediction: mock.Mock,
        current_rate: Union[int, float],
        exchange_rate_prediction: Union[int, float],
        result: str) -> None:
    mock_get_prediction.return_value = exchange_rate_prediction
    assert cryptocurrency_action(current_rate) == result
