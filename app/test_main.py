from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted, expected_result",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 103.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing")
    ],
)
def test_prediction(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: float,
    predicted: float,
    expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: predicted
    )
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
