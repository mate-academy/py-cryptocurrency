from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected_result",
    [
        (10, 10.6, "Buy more cryptocurrency"),
        (10, 9.4, "Sell all your cryptocurrency"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: int | float,
        exchange_rate: float,
        expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda *args: exchange_rate
    )
    assert cryptocurrency_action(current_rate) == expected_result
