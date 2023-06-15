from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, result",
    [
        (100, 200, "Buy more cryptocurrency"),
        (100, 50, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing")
    ]
)
@mock.patch("main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction, current_rate, prediction, result):
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == result
