from typing import Any

import pytest
from app import main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected",
    [
        pytest.param(20, 10, "Buy more cryptocurrency"),
        pytest.param(4, 10, "Sell all your cryptocurrency"),
        pytest.param(10.2, 10, "Do nothing"),
        pytest.param(95, 100, "Do nothing"),
        pytest.param(105, 100, "Do nothing"),
    ]
)
def test_can_calculate_cryptocurrency_action(
    monkeypatch: Any ,
    prediction_rate: float | int,
    current_rate: float | int,
    expected: str
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda ex_rate: prediction_rate)

    assert cryptocurrency_action(current_rate) == expected
