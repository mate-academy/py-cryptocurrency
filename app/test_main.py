import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.0, 1.03, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: object,
        current_rate: [int, float],
        prediction_rate: [int, float],
        expected_result: str
) -> None:
    def get_prediction(rate: [int, float]) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        get_prediction
    )
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
