import pytest
from app.main import cryptocurrency_action
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104.99, "Do nothing"),
        (100, 95.01, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: float,
        predicted_rate: float,
        expected_action: str
) -> None:
    def fake_prediction(rate: float) -> float:
        return predicted_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_prediction)

    assert cryptocurrency_action(current_rate) == expected_action
