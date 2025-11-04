from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, predict_rate, expected",
    [
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (5, 5.26, "Buy more cryptocurrency"),
        (5, 4.74, "Sell all your cryptocurrency"),
        (5, 5.25, "Do nothing"),
        (5, 4.75, "Do nothing"),
        (5.0, 5.3, "Buy more cryptocurrency"),
        (5.0, 4.6, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action_valid(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: int | float,
        predict_rate: int | float,
        expected: str
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: predict_rate)
    result = cryptocurrency_action(current_rate)
    assert result == expected
