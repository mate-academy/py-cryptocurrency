import pytest
from unittest.mock import MagicMock
import app.main as main


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
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
def test_cryptocurrency_action_with_mock(monkeypatch, current_rate, predicted_rate, expected):
    mock = MagicMock(return_value=predicted_rate)
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock)

    result = main.cryptocurrency_action(current_rate)

    assert result == expected
    mock.assert_called_once_with(current_rate)
