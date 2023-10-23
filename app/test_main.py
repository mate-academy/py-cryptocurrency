# write your code here
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, result",
    [
        (1, 1, "Do nothing"),
        (1, 0.93, "Sell all your cryptocurrency"),
        (1, 1.01, "Do nothing"),
        (1, 1.07, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_get_exchange_rate_prediction: mock,
        current_rate: int | float,
        predict_rate: int | float,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == result
