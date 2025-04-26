from typing import Any

import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_multiplier, expected_action",
    [
        (100, 1.05, "Do nothing"),
        (100, 0.95, "Do nothing"),
    ]
)
def test_do_nothing_on_95_and_105_percent(
        monkeypatch: Any,
        current_rate: int,
        prediction_multiplier: int,
        expected_action: str
) -> None:
    def mock_prediction(rate: Any) -> None:
        return rate * prediction_multiplier

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    result = cryptocurrency_action(current_rate)
    assert result == expected_action, (
        f"When prediction_rate is exactly {prediction_multiplier * 100.0} "
        f"of current_rate, the function must return '{expected_action}'."
    )
