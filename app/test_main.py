import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected",
    [
        (1, 2, "Buy more cryptocurrency"),
        (2, 1, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (1, 1, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: bool,
    exchange_rate: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: exchange_rate,
    )

    assert cryptocurrency_action(current_rate) == expected
