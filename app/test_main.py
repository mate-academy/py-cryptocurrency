import pytest
from app.main import cryptocurrency_action
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "rate_multiplier, expected_action",
    [
        (1.06, "Buy more cryptocurrency"),  # > 5% higher
        (0.94, "Sell all your cryptocurrency"),  # > 5% lower
        (1.05, "Do nothing"),  # exactly 5% higher (boundary)
        (0.95, "Do nothing"),  # exactly 5% lower (boundary)
        (1.0, "Do nothing"),  # stable
        (1.02, "Do nothing"),  # within the +/- 5% range
    ],
)
def test_cryptocurrency_action(
    monkeypatch: MonkeyPatch, rate_multiplier: float, expected_action: str
) -> None:
    """Tests cryptocurrency_action with various predicted rate changes."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * rate_multiplier,
    )
    assert cryptocurrency_action(100) == expected_action
