from collections.abc import Callable

import pytest

from app import main


@pytest.fixture
def set_prediction(
    monkeypatch: pytest.MonkeyPatch,
) -> Callable[[float], None]:
    def set_prediction_rate(prediction_rate: float) -> None:
        monkeypatch.setattr(
            main,
            "get_exchange_rate_prediction",
            lambda exchange_rate: prediction_rate,
        )

    return set_prediction_rate


@pytest.mark.parametrize(
    ("prediction_rate", "current_rate", "expected_action"),
    [
        (105, 100, "Do nothing"),
        (2.1, 2, "Do nothing"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (1.9, 2, "Do nothing"),
        (10, 5, "Buy more cryptocurrency"),
        (8.53, 3.76, "Buy more cryptocurrency"),
        (8.53, 5, "Buy more cryptocurrency"),
        (9, 7.34, "Buy more cryptocurrency"),
        (34, 61, "Sell all your cryptocurrency"),
        (23.45, 144.01, "Sell all your cryptocurrency"),
        (57.85, 70, "Sell all your cryptocurrency"),
        (94, 102.43, "Sell all your cryptocurrency"),
    ],
)
def test_action_for_prediction(
    set_prediction: Callable[[float], None],
    current_rate: float,
    prediction_rate: float,
    expected_action: str,
) -> None:
    set_prediction(prediction_rate)

    assert main.cryptocurrency_action(current_rate) == expected_action
