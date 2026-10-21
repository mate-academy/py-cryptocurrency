import pytest

from app import main


@pytest.mark.parametrize(
    ("prediction_rate", "expected_action"),
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    prediction_rate: float,
    expected_action: str,
) -> None:
    current_rate = 100
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: prediction_rate
    )

    assert main.cryptocurrency_action(current_rate) == expected_action
