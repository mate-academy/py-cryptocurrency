from typing import Union

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,"
    "prediction_rate,"
    "expecting_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expecting_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expecting_result
