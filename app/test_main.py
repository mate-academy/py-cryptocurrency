import pytest
from typing import Union
import app.main as main


@pytest.mark.parametrize(
    "exchange_rate_prediction, current_rate, result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (2.1, 2, "Do nothing"),
        (1.9, 2, "Do nothing")
    ]
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    exchange_rate_prediction: float,
    current_rate: Union[int, float],
    result: str
) -> None:

    def monkey_get_exchange_rate_prediction(
        current_rate: Union[int, float]
    ) -> float:
        return exchange_rate_prediction

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        monkey_get_exchange_rate_prediction
    )
    assert main.cryptocurrency_action(current_rate) == result
