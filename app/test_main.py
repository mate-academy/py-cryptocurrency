import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 2.2, "Buy more cryptocurrency"),
        (2, 1.0, "Sell all your cryptocurrency"),
        (1.0, 1.0, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ],
    ids=[
        "buy more action",
        "sell all action",
        "do nothing action",
        "rate ratio 0,95",
        "rate ratio 1,05"
    ]
)
def test_cryptocurrency_action(
    monkeypatch: MonkeyPatch,
    current_rate: int | float,
    prediction_rate: float,
    expected: str
) -> None:
    def mock_get_exchange_rate_prediction(*args: int | float) -> float:
        print(f"mock_get_exchange_rate_prediction called with {args}")
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert (
        cryptocurrency_action(current_rate) == expected
    ), f"Returned actions should be: '{expected}'"
