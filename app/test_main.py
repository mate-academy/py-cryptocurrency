import pytest
from pytest import MonkeyPatch
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "current_rate, multiple, expected",
    [
        (100, 1.06, "Buy more cryptocurrency"),
        (100, 0.94, "Sell all your cryptocurrency"),
        (100, 1.03, "Do nothing"),
        (50, 1.05, "Do nothing"),
        (50, 0.95, "Do nothing"),
    ],
    ids=[
        "buy_more",
        "sell_all",
        "do_nothing_small_increase",
        "boundary_1_05",
        "boundary_0_95",
    ]
)
def test_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        current_rate: Union[int, float],
        multiple: float,
        expected: str
) -> None:
    def mock_prediction(rate: Union[int, float]) -> Union[int, float]:
        return rate * multiple
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(current_rate) == expected
