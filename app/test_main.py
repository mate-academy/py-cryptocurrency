from typing import Any, Union

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (10, 10, "Do nothing"),
        (10, 9.5, "Do nothing"),
        (10, 10.5, "Do nothing"),
        (10, 5, "Sell all your cryptocurrency"),
        (10, 20, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: Any,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: prediction_rate
    )

    assert cryptocurrency_action(current_rate) == result
