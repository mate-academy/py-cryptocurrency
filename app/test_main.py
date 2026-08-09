import pytest
from pytest import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 102.0, "Do nothing"),
        (100.0, 98.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action_scenarios(
    monkeypatch: MonkeyPatch,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: predicted_rate,
    )

    result = cryptocurrency_action(current_rate)

    assert result == expected

    result = cryptocurrency_action(current_rate)

    assert result == expected
