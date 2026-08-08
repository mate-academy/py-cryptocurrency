from app.main import cryptocurrency_action
from unittest import mock

import pytest


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (10, 10, "Do nothing"),
        (10, 5, "Sell all your cryptocurrency"),
        (10, 12, "Buy more cryptocurrency"),
        (10, 9.5, "Do nothing"),
        (10, 10.5, "Do nothing")
    ],
    ids=[
        "prediction_rate = current_rate -> should return 'Do nothing'",
        "prediction_rate = 0.5 * current_rate -> should return 'Sell'",
        "prediction_rate = 1.2 * current_rate -> should return 'Buy more'",
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95",
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        predicted_rate: int | float,
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == expected_result
