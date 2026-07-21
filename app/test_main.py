import pytest
from app import main
from typing import Callable


@pytest.mark.parametrize(
    "predicted_rate, expected_result",
    [
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing")
    ]
)
def test_should_return_expected_result(
        predicted_rate: float,
        expected_result: str,
        monkeypatch: Callable
) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return current_rate * predicted_rate
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert main.cryptocurrency_action(100) == expected_result
