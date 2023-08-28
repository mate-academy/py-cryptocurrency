from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        (10, 9.5, "Sell all your cryptocurrency"),
        (10, 10.5, "Buy more cryptocurrency"),
        (10, 10, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        exchange_rate: int,
        result: str,
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda *args: exchange_rate
    )
    assert cryptocurrency_action(current_rate) == result
