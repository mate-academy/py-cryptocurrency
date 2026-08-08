import pytest
from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted, current, expected",
    [
        pytest.param(
            112,
            100,
            "Buy more cryptocurrency",
            id="test prediction = 112 - buy more"
        ),
        pytest.param(
            110,
            100,
            "Buy more cryptocurrency",
            id="test prediction = 110 - buy more"
        ),

        pytest.param(
            105,
            100,
            "Do nothing",
            id="test prediction = 105 - do nothing"
        ),
        pytest.param(
            103,
            100,
            "Do nothing",
            id="test prediction = 103 - do nothing"
        ),
        pytest.param(
            95,
            100,
            "Do nothing",
            id="test prediction = 95 - do nothing"
        ),
        pytest.param(
            97,
            100,
            "Do nothing",
            id="test prediction = 97 - do nothing"
        ),

        pytest.param(
            92,
            100,
            "Sell all your cryptocurrency",
            id="test prediction = 92 - sell your cryptocurrency"
        ),
        pytest.param(
            88,
            100,
            "Sell all your cryptocurrency",
            id="test prediction = 88 - sell your cryptocurrency"
        ),
    ],
)
def test_cryptocurrency_action(
        predicted: Union[int, float],
        current: Union[int, float],
        expected: str) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=predicted
    ):
        assert cryptocurrency_action(current) == expected
