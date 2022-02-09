from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected_result",
    [
        pytest.param(
            1.0, 1.1,
            "Sell all your cryptocurrency",
            id="test prediction for decreasing"
        ),
        pytest.param(
            1.1, 1.0,
            "Buy more cryptocurrency",
            id="test prediction for increasing"
        ),
        pytest.param(
            1.30, 1.25,
            "Do nothing",
            id="test without changes -5%"
        ),
        pytest.param(
            1.8, 1.85,
            "Do nothing",
            id="test without changes +5%)"
        ),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate,
        exchange_rate,
        current_rate,
        expected_result
):
    mocked_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
