from typing import Union
from unittest.mock import MagicMock
import pytest
import app.main as main
from _pytest.monkeypatch import MonkeyPatch
Rate = Union[int, float]


@pytest.mark.parametrize(
    ("current_rate", "predicted_rate", "expected"),
    [
        (100, 106, "Buy more cryptocurrency"),
        (10.0, 10.7, "Buy more cryptocurrency"),

        (100, 94, "Sell all your cryptocurrency"),
        (10.0, 9.4, "Sell all your cryptocurrency"),

        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),

        (200, 201, "Do nothing"),
    ],
)
def test_cryptocurrency_action_with_mock(
    monkeypatch: MonkeyPatch,
    current_rate: Rate,
    predicted_rate: Rate,
    expected: str,
) -> None:
    mock = MagicMock(return_value=predicted_rate)
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock)

    result = main.cryptocurrency_action(current_rate)

    assert result == expected
    mock.assert_called_once_with(current_rate)
