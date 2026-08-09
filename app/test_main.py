import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        pytest.param(
            100,
            105,
            "Do nothing",
            id="do nothing when rate is 1.05 percent"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="do nothing when rate is 0.95 percent"
        ),
        pytest.param(
            100,
            200,
            "Buy more cryptocurrency",
            id="buy more when rate is more than 1.05 percent"
        ),
        pytest.param(
            100,
            50,
            "Sell all your cryptocurrency",
            id="sell all when rate is less than 0.95 percent"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_walid_change(
        mocked_exchange_rate,
        current_rate,
        prediction_rate,
        expected_result):

    mocked_exchange_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
