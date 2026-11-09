import pytest
import app.main as main


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: int,
    prediction_rate: int,
    expected: str,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: prediction_rate,
    )

    assert main.cryptocurrency_action(current_rate) == expected
