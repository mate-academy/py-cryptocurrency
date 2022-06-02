from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,result_message",
    [
        pytest.param(
            2,
            2.5,
            "Buy more cryptocurrency",
            id="Should predict sell when cost increase"
        ),
        pytest.param(
            2,
            1.5,
            "Sell all your cryptocurrency",
            id="Should predict sell when cost decrease"
        ),
        pytest.param(
            2,
            2.1,
            "Do nothing",
            id="Should do nothing when small increase"
        ),
        pytest.param(
            2,
            1.9,
            "Do nothing",
            id="Should do nothing when small decrease"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_called_get(
    mocked_exchange_func,
    current_rate,
    exchange_rate,
    result_message
):
    mocked_exchange_func.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == result_message
