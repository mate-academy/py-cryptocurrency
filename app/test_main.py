from __future__ import annotations

import pytest
from app.main import cryptocurrency_action

from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (50, 110, "Buy more cryptocurrency"),
        (150, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")

    ],
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: int | float,
        prediction_rate: int | float,
        expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: prediction_rate
    )
    assert cryptocurrency_action(current_rate) == expected_result
