import pytest
from typing import Any
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current, percent, result",
    [
        (100, 1.5, "Buy more cryptocurrency"),
        (100, 1.05, "Do nothing"),
        (100, 0.95, "Do nothing"),
        (100, 0.94, "Sell all your cryptocurrency"),
    ]
)
def test_should_return_to_manage_finances(
    monkeypatch: Any,
    current: int,
    percent: float | int,
    result: str
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: current * percent
                        )
    assert cryptocurrency_action(current) == result
