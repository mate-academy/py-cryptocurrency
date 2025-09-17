from unittest.mock import Mock

import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("current", "mult", "expected"),
    [
        (100.0, 1.0501, "Buy more cryptocurrency"),        # > +5%
        (100.0, 0.9499, "Sell all your cryptocurrency"),   # < -5%
        (100.0, 1.0300, "Do nothing"),                     # між межами
        (100.0, 1.0500, "Do nothing"),                     # рівно +5%
        (100.0, 0.9500, "Do nothing"),                     # рівно -5%
    ],
)
def test_cryptocurrency_action_decisions(
    monkeypatch: MonkeyPatch,
    current: float,
    mult: float,
    expected: str,
) -> None:
    predicted = current * mult
    predictor = Mock(return_value=predicted)
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", predictor)

    result = cryptocurrency_action(current)

    assert result == expected
    predictor.assert_called_once_with(current)


def test_cryptocurrency_action_uses_percentage_not_delta(
    monkeypatch: MonkeyPatch,
) -> None:
    current = 80.0
    predicted = 84.1
    predictor = Mock(return_value=predicted)
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", predictor)

    result = cryptocurrency_action(current)

    assert result == "Buy more cryptocurrency"
    predictor.assert_called_once_with(current)
