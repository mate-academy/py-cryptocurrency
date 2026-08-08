from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current_rate, result",
    [
        (23, 21, "Buy more cryptocurrency"),
        (21, 23, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_func,
        exchange_rate,
        current_rate,
        result
):
    mocked_func.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result
