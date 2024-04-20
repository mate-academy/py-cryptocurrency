from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "c_rate,func,answer",
    [
        pytest.param(
            1,
            1.06,
            "Buy more cryptocurrency",
            id="should buy"
        ),
        pytest.param(
            1,
            0.94,
            "Sell all your cryptocurrency",
            id="should sell",
        ),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="should hold"
        ),
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="should hold"
        )
    ]
)
def test(c_rate,
         func,
         answer):
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=func):
        assert cryptocurrency_action(c_rate) == answer
