from typing import Union

import pytest

from app import main
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,result",
    [
        pytest.param(
            105, "Do nothing",
            id="Do nothing if 5% increase"
        ),
        pytest.param(
            105.01, "Buy more cryptocurrency",
            id="Buy more cryptocurrency if 5.01% increase"
        ),
        pytest.param(
            95, "Do nothing",
            id="Do nothing if 5% decrease"
        ),
        pytest.param(
            94.99, "Sell all your cryptocurrency",
            id="Sell all cryptocurrency if 5.01% decrease"
        ),
    ]
)
def test_cryptocurrency_action(
        monkeypatch: callable,
        predicted_rate: Union[int, float],
        result: str
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda _: predicted_rate
    )
    assert cryptocurrency_action(100) == result
