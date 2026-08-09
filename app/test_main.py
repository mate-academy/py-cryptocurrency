import pytest
import app.main as main


@pytest.mark.parametrize(
    "exchange_rate, expected",
    [
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
        (0.94, "Sell all your cryptocurrency"),
        (1.06, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        exchange_rate: int | float,
        expected: str
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: current_rate * exchange_rate
    )
    assert main.cryptocurrency_action(100) == expected
