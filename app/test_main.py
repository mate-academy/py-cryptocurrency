import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction,action",
    [
        (0.84, "Sell all your cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.00, "Do nothing"),
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),
        (2.00, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        prediction: float,
        action: str
) -> None:
    def mock_prediction(current_rate: int | float) -> float:
        return prediction

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )
    assert cryptocurrency_action(1) == action
