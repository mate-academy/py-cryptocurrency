from unittest import mock

import pytest

from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "current, predicted, result",
    [
        pytest.param(
            100,
            106,
            "Buy more cryptocurrency",
            id="Buy more if projected growth is over 5%"
        ),
        pytest.param(
            100,
            94,
            "Sell all your cryptocurrency",
            id="Sell all if the predicted rate falls by more than 5% from the current"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="Do nothing if no big changes predicted"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="Do nothing if no big changes predicted"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate,
        current,
        predicted,
        result
):
    mocked_exchange_rate.return_value = predicted
    assert cryptocurrency_action(current) == result
