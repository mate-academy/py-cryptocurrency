from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current,exchange_rate,result",
    [
        pytest.param(
            100,
            110,
            "Buy more cryptocurrency"
        ),
        pytest.param(
            100,
            90,
            "Sell all your cryptocurrency"
        ),
        pytest.param(
            100,
            98,
            "Do nothing"
        ),
        pytest.param(
            100,
            105,
            "Do nothing"
        ),
        pytest.param(
            100,
            95,
            "Do nothing"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange,
        current,
        exchange_rate,
        result
):
    mocked_exchange.return_value = exchange_rate

    assert cryptocurrency_action(current) == result
