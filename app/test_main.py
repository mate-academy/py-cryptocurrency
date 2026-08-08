from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict_rate, current_rate, result",
    [
        (110, 100, "Buy more cryptocurrency"),
        (89, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ],
    ids=[
        "Should buy coins when prediction / current rate > 1.05",
        "Should sell coins when prediction / current rate < 0.95",
        "Should not buy coins when prediction / current rate == 1.05",
        "Should not sell coins when prediction / current rate == 0.95",

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        predict_rate: Union[int, float],
        current_rate: Union[int, float],
        result: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == result
