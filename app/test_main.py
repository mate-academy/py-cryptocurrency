from typing import Any
from app import main
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction, rate, expected",
    [
        pytest.param(1.06, 1, "Buy more cryptocurrency"),
        pytest.param(0.94, 1, "Sell all your cryptocurrency"),
        pytest.param(0.95, 1, "Do nothing"),
        pytest.param(1.05, 1, "Do nothing"),
    ],
)
def test_should_return_correct_result(monkeypatch: Any,
                                      prediction: int | float,
                                      rate: int | float,
                                      expected: str) -> None:
    def mock_predict(rate: int | float) -> int | float:
        return prediction
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_predict)
    assert cryptocurrency_action(rate) == expected
