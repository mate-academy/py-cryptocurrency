import pytest
from app import main


@pytest.mark.parametrize(
    "predict, current, expected",
    [
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (0.98, 1, "Do nothing"),
        (0.93, 1, "Sell all your cryptocurrency"),
        (1.11, 1, "Buy more cryptocurrency"),
    ],
    ids=[
        "boundary_1.05_do_nothing",
        "boundary_0.95_do_nothing",
        "within_range_do_nothing",
        "below_0.95_sell",
        "above_1.05_buy",
    ]
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    predict: float,
    current: int,
    expected: str
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current: predict)
    assert main.cryptocurrency_action(current) == expected
