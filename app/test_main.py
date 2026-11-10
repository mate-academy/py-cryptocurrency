from _pytest.monkeypatch import MonkeyPatch
from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda exchange_rate: prediction_rate)
    result = cryptocurrency_action(current_rate)
    assert result == expected
