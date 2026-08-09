from typing import Any
from typing import Union
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_prediction, current_rate, expected_result",
    [
        (10.71, 10, "Buy more cryptocurrency"),
        (9.21, 10, "Sell all your cryptocurrency"),
        (10.01, 10, "Do nothing"),
        (10.5, 10, "Do nothing"),
        (9.5, 10, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    monkeypatch: Any,
    exchange_rate_prediction: Union[int, float],
    current_rate: Union[int, float],
    expected_result: str
) -> None:

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: exchange_rate_prediction
    )
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
