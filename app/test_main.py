from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            100,
            105,
            "Do nothing",
            id="do nothing if rate 1,05"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="do nothing if rate 0,95"
        ),
        pytest.param(
            100,
            110,
            "Buy more cryptocurrency",
            id="buy more if rate > 1,05"
        ),
        pytest.param(
            100,
            90,
            "Sell all your cryptocurrency",
            id="sell all if rate < 0,95"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction_rate, current_rate, prediction_rate, expected):
    mocked_prediction_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected

