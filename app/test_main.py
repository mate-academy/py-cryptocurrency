import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),          # +6% -> buy
        (100, 94, "Sell all your cryptocurrency"),      # -6% -> sell
        (100, 104, "Do nothing"),                       # +4% -> nothing
        (100, 96, "Do nothing"),                        # -4% -> nothing
        (100, 105, "Do nothing"),                       # exactly +5% -> nothing
        (100, 95, "Do nothing"),                        # exactly -5% -> nothing
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    def mock_get_exchange_rate_prediction(_current_rate: float) -> float:
        return predicted_rate

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert main.cryptocurrency_action(current_rate) == expected
