import pytest
from app.main import cryptocurrency_action
from typing import Any


@pytest.mark.parametrize(
    "current_rate, prediction, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 153, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 100, "Do nothing")
    ]
)
def test_crypto_action_function(
    monkeypatch: Any,
    current_rate: int,
    prediction: int,
    expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: prediction
    )
    assert cryptocurrency_action(current_rate) == expected
