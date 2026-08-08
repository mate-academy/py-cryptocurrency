from typing import Any

from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, action",
    [
        # BUY (> +5%)
        (100, 106, "Buy more cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),

        # SELL (< -5%)
        (100, 94, "Sell all your cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),

        # DO NOTHING (boundary included)
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (200, 210, "Do nothing"),
        (200, 190, "Do nothing"),

        # neutral
        (100, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(current_rate: Any,
                               prediction_rate: Any,
                               action: Any) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = prediction_rate
        result = cryptocurrency_action(current_rate)
        assert result == action
        mocked_get_exchange_rate_prediction.assert_called_once()
