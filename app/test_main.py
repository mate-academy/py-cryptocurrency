import pytest
from unittest.mock import Mock
import app.main as main
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 102, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: float,
        predicted_rate: float,
        expected: str,
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main,
                        "get_exchange_rate_prediction",
                        Mock(return_value=predicted_rate)
                        )
    result = main.cryptocurrency_action(current_rate)
    assert result == expected
