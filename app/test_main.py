from app.main import cryptocurrency_action

from unittest import mock
from typing import Any

import pytest


# @mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "mocked_return_value,current_rate,expected_value",
    [
        pytest.param(
            2,
            1.15,
            "Buy more cryptocurrency",
            id="test cryptocurrency action "
               "get return Buy more cryptocurrency"
        ),
        pytest.param(
            1.05,
            1.15,
            "Sell all your cryptocurrency",
            id="test cryptocurrency action "
               "get return Sell all your cryptocurrency"
        ),
        pytest.param(
            1.15,
            1.15,
            "Do nothing",
            id="test cryptocurrency action "
               "get return Do nothing"
        ),
        pytest.param(
            1.2075,
            1.15,
            "Do nothing",
            id="test cryptocurrency action "
               "1.05 Do nothing"
        ),
        pytest.param(
            1.219,
            1.15,
            "Buy more cryptocurrency",
            id="test cryptocurrency action "
               "1.06 Buy more cryptocurrency"
        ),
        pytest.param(
            1.9,
            2,
            "Do nothing",
            id="test cryptocurrency action "
               "0.95 Do nothing"
        ),
        pytest.param(
            1.081,
            1.15,
            "Sell all your cryptocurrency",
            id="test cryptocurrency action "
               "0.94 Sell all your cryptocurrency"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mocked_get_exchange_rate_prediction: Any,
        mocked_return_value: int,
        current_rate: int,
        expected_value: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = mocked_return_value
    assert cryptocurrency_action(current_rate) == expected_value
