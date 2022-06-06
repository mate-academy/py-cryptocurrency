from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, returned_msg",
    [
        pytest.param(
            2, 1.5, "Buy more cryptocurrency",
            id="Need to buy"
        ),

        pytest.param(
            1.5, 2, "Sell all your cryptocurrency",
            id="Need to sell"
        ),

        pytest.param(
            1.05, 1, "Do nothing",
            id="Need nothing to do while increase == 1.05"
        ),

        pytest.param(
            0.95, 1, "Do nothing",
            id="Need nothing to do while decrease == 0.95"
        )
    ]

)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_called_get(mocked_func,
                    prediction_rate,
                    current_rate,
                    returned_msg):

    mocked_func.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == returned_msg
