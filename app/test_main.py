from typing import Any, Union
from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 1.05, "Buy more cryptocurrency"),
        (1, 0.95, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        monkeypatch: Any,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]
    ) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )

    assert cryptocurrency_action(current_rate) == expected
