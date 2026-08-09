from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> Mock:
    with patch("app.main.get_exchange_rate_prediction") as mock_get_rate:
        yield mock_get_rate


@pytest.mark.parametrize(
    "current_rate, predicted_rate, action",
    [
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency")
    ],
    ids=[
        "lower border for do nothing scenario",
        "upper border for do nothing scenario",
        "check if recommends to buy cryptocurrency",
        "check if recommends to sell cryptocurrency"
    ]
)
def test_main_cases_for_cryptocurrency_action(
        current_rate: int | float,
        predicted_rate: float,
        action: str,
        mock_get_exchange_rate_prediction: Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == action
