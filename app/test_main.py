import pytest
from app.main import cryptocurrency_action
from typing import Union
import app


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (1, 5, "Buy more cryptocurrency"),
        (2, 2.1, "Do nothing"),
        (1, 0.8, "Sell all your cryptocurrency"),
        (6, 6, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    def give_preset_exchange_rate(exchange_rate: Union[int, float]) -> float:
        return prediction_rate
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        give_preset_exchange_rate
    )
    assert (
        cryptocurrency_action(current_rate) == expected_result
    ), f"if a rate changes from {current_rate} to " \
       f"{prediction_rate} then a result should be {expected_result}"
