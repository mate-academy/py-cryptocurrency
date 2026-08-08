import pytest
from pytest import MonkeyPatch

import app.main


@pytest.mark.parametrize(
    "current_rate,mocked_rate,result",
    [
        (1.0, 2.0, "Buy more cryptocurrency"),
        (2.25, 2.0, "Sell all your cryptocurrency"),
        (2, 2.0, "Do nothing"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ],
    ids=[
        "Buy more",
        "Sell all",
        "Nothing 1",
        "Nothing 2",
        "Nothing 3"
    ]
)
def test_cryptocurrency_action(
    monkeypatch: MonkeyPatch,
    current_rate: float | int,
    mocked_rate: float,
    result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: mocked_rate
    )
    assert (
        app.main.cryptocurrency_action(current_rate) == result
    ), "Result is not expected"
