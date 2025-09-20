import app.main
import pytest
from app.main import cryptocurrency_action
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "current_rate, predict_rate, result",
    [
        (50, 100, "Buy more cryptocurrency"),
        (200, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               predict_rate: int | float,
                               result: str,
                               monkeypatch: MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(current_rate: int | float) -> None:
        return predict_rate
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(current_rate) == result
