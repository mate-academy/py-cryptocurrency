
import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: float,
    prediction_rate: float,
    expected: str,
) -> None:
    def mock_prediction(exchange_rate: int | float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_prediction,
    )

    result = main.cryptocurrency_action(current_rate)

    assert result == expected
