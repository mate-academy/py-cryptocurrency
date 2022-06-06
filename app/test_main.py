import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current, predict, result",
    [
        (15, 20, "Buy more cryptocurrency"),
        (16, 15, "Sell all your cryptocurrency"),
        (15, 15, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_func, current, predict, result):
    mocked_func.return_value = predict
    assert cryptocurrency_action(current) == result
