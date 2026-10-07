from unittest.mock import Mock

import pytest

from app import main


@pytest.mark.parametrize(
    ("prediction_rate", "expected"),
    [
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    prediction_rate: float,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    current_rate = 100
    prediction_mock = Mock(return_value=prediction_rate)
    monkeypatch.setattr(main, "get_exchange_rate_prediction", prediction_mock)

    assert main.cryptocurrency_action(current_rate) == expected
    prediction_mock.assert_called_once_with(current_rate)
