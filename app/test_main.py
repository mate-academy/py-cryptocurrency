import pytest

from app import main


@pytest.mark.parametrize(
    ("prediction_rate", "expected_action"),
    [
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    prediction_rate: float,
    expected_action: str,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: prediction_rate,
    )

    assert main.cryptocurrency_action(100) == expected_action
