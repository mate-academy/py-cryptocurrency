import pytest
from app import main
from typing import Union

def patch_prediction(
        monkeypatch,
        return_value: float
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda rate: return_value)


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (200.0, 211.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (150.0, 140.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 102.0, "Do nothing"),
        (100.0, 98.0, "Do nothing"),
        (100.0, 105.000001, "Buy more cryptocurrency"),
        (100.0, 94.999999, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected: str
) -> None:
    patch_prediction(monkeypatch, predicted_rate)
    result = main.cryptocurrency_action(current_rate)
    assert result == expected
