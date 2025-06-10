import pytest

from app import main
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "prediction_exchange_rate, current_exchange_rate, expected_action",
    [
        (1.66, 0.66, "Buy more cryptocurrency"),
        (1.66, 1.96, "Sell all your cryptocurrency"),
        (1.05, 1.00, "Do nothing"),
        (0.95, 1.00, "Do nothing"),
    ],
    ids=[
        "buy more", "sell all",
        "do nothing exact 1.05",
        "do nothing exact 0.95"
    ]
)
def test_action_buy_more(
        monkeypatch: MonkeyPatch,
        prediction_exchange_rate: float,
        current_exchange_rate: float,
        expected_action: str
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction",
        lambda exchange_rate: prediction_exchange_rate
    )
    actual_action = main.cryptocurrency_action(current_exchange_rate)
    assert actual_action == expected_action
