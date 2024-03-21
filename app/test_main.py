import pytest
from typing import Callable

import app.main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_exchange, result", [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 0.96, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
def test_get_exchange_rate_prediction_with_mock(monkeypatch: Callable,
                                                current_rate: float,
                                                predicted_exchange: float,
                                                result: str) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return predicted_exchange

    monkeypatch.setattr(target=app.main,
                        name="get_exchange_rate_prediction",
                        value=mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(current_rate) == result
