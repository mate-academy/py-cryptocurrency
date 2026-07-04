import pytest
from app import main


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: float,
        prediction_rate: float,
        expected: str,
) -> None:

    def mock_prediction(rate: float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction,
    )

    result = main.cryptocurrency_action(current_rate)
    assert result == expected
