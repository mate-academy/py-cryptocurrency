import pytest
from unittest.mock import Mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (1, 1, "Do nothing"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.92, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    prediction_rate: float,
    expected_action: str,
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        Mock(return_value=prediction_rate)
    )

    assert cryptocurrency_action(current_rate) == expected_action
