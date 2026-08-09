from typing import Any

from app import main
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction, rate, expected_result",
    [
        pytest.param(1.05, 1, "Do nothing", id="should not buy"),
        pytest.param(0.95, 1, "Do nothing", id="should not sell"),
    ],
)
def test_should_return_correct_string(
    monkeypatch: Any,
    prediction: int | float,
    rate: int | float,
    expected_result: str,
) -> None:
    def mock_prediction(current_rate: int | float) -> int:
        return prediction

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)

    assert cryptocurrency_action(rate) == expected_result
