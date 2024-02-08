from app.main import cryptocurrency_action
from unittest import mock
import pytest

@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, message",
    [
        (6000, 10000, "Buy more cryptocurrency"),
        (6000, 1000, "Sell all your cryptocurrency"),
        (1000, 1000, "Do nothing"),
    ]
)
def test_cannot_access_if_only_valid_url(mocked_func, current_rate, predicted_rate, message):
    mocked_func.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == message
