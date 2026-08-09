import pytest
from _pytest.monkeypatch import MonkeyPatch

import app.main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_output",
    [
        (1000, 950, "Buy more cryptocurrency"),
        (1000, 1050, "Do nothing"),
        (900, 1000, "Sell all your cryptocurrency"),
        (1050, 1000, "Do nothing"),
        (950, 1000, "Do nothing")
    ]
)
def test_verify_correct_work_of_cryptocurrency_action(
        monkeypatch: MonkeyPatch,
        prediction_rate: int,
        current_rate: int,
        expected_output: str
) -> None:
    def mock_prediction(_: int | float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_prediction
    )
    assert cryptocurrency_action(current_rate) == expected_output
