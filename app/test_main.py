import pytest
from typing import Union
from app import main


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected",
    [
        (5, 22.96, "Buy more cryptocurrency"),
        (8, 2.87, "Sell all your cryptocurrency"),
        (3.32, 3.35, "Do nothing"),
        (1.23, 1.22, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: Union[int, float],
    exchange_rate: float,
    expected: str,
) -> None:
    # Mock de get_exchange_rate_prediction
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda _: exchange_rate,
    )

    result = main.cryptocurrency_action(current_rate)
    assert result == expected
