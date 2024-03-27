from __future__ import annotations

from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current_rate, expected_result",
    [(80, 5, "Buy more cryptocurrency"),
     (2, 5, "Sell all your cryptocurrency"),
     (4.75, 5, "Do nothing"),
     (5.25, 5, "Do nothing")]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate(
        mock_get_exchange_rate_prediction: pytest.param,
        exchange_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
