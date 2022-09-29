import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value,prediction_of_value,expected",
    [
        pytest.param(1, 1.1, "Buy more cryptocurrency"),
        pytest.param(1, 0.87, "Sell all your cryptocurrency"),
        pytest.param(1, 1.05, "Do nothing"),
        pytest.param(1, 0.95, "Do nothing"),
        pytest.param(2, 2.5, "Buy more cryptocurrency"),
        pytest.param(9, 2.5, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_of_our_seller_buyer(mocked, value, prediction_of_value, expected):
    mocked.return_value = prediction_of_value
    assert cryptocurrency_action(current_rate=value) == expected
