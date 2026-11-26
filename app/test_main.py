import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: float,
        predicted_rate: float,
        expected: str
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: predicted_rate
    )

    assert main.cryptocurrency_action(current_rate) == expected
