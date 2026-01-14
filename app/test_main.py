from typing import Union

import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 100, "Do nothing"),
        (200, 211, "Buy more cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
    ],
    ids=[
        "Buy more, more than 5 percent higher from the current",
        "Sell all, more than 5 percent lower from the current",
        "Do nothing at 5 percent increase",
        "Do nothing at 5 percent decrease",
        "Do nothing slight increase",
        "Do nothing slight decrease",
        "Do nothing no change",
        "Buy more with different rate",
        "Sell all with different rate"
    ]
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: int,
        predicted_rate: int,
        expected: str
) -> None:
    def mock_predicted_rate(*args) -> Union[int, float]:
        return predicted_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_predicted_rate
    )
    result = cryptocurrency_action(current_rate)

    assert result == expected
