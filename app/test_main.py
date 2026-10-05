import pytest
from pytest import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (94.99, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (95.01, "Do nothing"),
        (100, "Do nothing"),
        (104.99, "Do nothing"),
        (105, "Do nothing"),
        (105.01, "Buy more cryptocurrency"),
    ],
)
def test_prediction_thresholds(
    monkeypatch: MonkeyPatch, prediction: float, expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: prediction
    )
    assert cryptocurrency_action(100) == expected
