
from unittest.mock import patch
from typing import Any, Union


import pytest


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction,current,result",
    [
        pytest.param(
            1.25,
            1.0,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency case"
        ),
        pytest.param(
            0.9,
            1.0,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency case"
        ),
        pytest.param(
            1.0,
            1.0,
            "Do nothing",
            id="Do nothing case"
        ),
        pytest.param(
            0.95,
            1.0,
            "Do nothing",
            id="Do nothing case"
        ),
        pytest.param(
            1.05,
            1.0,
            "Do nothing",
            id="Do nothing case"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: Any,
                               prediction: Union[int | float],
                               current: Union[int | float],
                               result: str) -> None:

    mocked_get_exchange_rate_prediction.return_value = prediction

    assert cryptocurrency_action(current) == result
