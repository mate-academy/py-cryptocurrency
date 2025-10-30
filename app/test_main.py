from typing import Any
from pytest import MonkeyPatch, mark, raises, param
from app.main import cryptocurrency_action
import app.main as main


@mark.parametrize("current_rate, mock_prediction_rate, result", [
    (1.0, 1.05, "Do nothing"),
    (1.0, 0.95, "Do nothing"),
    (1.0, 1.06, "Buy more cryptocurrency"),
    (1.0, 5.0, "Buy more cryptocurrency"),
    (1.0, 99.0, "Buy more cryptocurrency"),
    (1.0, 0.94, "Sell all your cryptocurrency")
])
def test_cryptocurrency_action_decision_logic(
        monkeypatch: MonkeyPatch,
        current_rate: float,
        mock_prediction_rate: float,
        result: str
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda x: mock_prediction_rate)

    assert cryptocurrency_action(current_rate) == result


@mark.parametrize("current_rate, mock_prediction_rate, expected_exc", [
    param(0.0, 1.05, ValueError, id="zero-rate"),
    param(-1.0, 1.05, ValueError, id="negative-rate"),
    param("1", 1.05, TypeError, id="string-rate"),
    param(None, 1.05, TypeError, id="none-rate")
])
def test_cryptocurrency_action_raises(monkeypatch: MonkeyPatch,
                                      current_rate: Any,
                                      mock_prediction_rate: int | float,
                                      expected_exc: object
                                      ) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda x: mock_prediction_rate)
    with raises(expected_exc):
        cryptocurrency_action(current_rate)
