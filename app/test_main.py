import pytest
from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_rate, expected_result",
    [
        pytest.param(
            7,
            7.85,
            "Buy more cryptocurrency",
            id="should buy more as predicted rate > 5%"
        ),
        pytest.param(
            7,
            6.5,
            "Sell all your cryptocurrency",
            id="should sell as predicted rate < 5%"
        ),
        pytest.param(
            25,
            23.75,
            "Do nothing",
            id="should do nothing with 0.95 rate"
        ),
        pytest.param(
            7,
            7.35,
            "Do nothing",
            id="should do nothing with 1.05 rate"
        )
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        expected_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=expected_rate):
        assert (cryptocurrency_action(current_rate) == expected_result)
