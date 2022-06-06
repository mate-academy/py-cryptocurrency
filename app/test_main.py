import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,current_rate,result",
    [
        pytest.param(2, 1, "Buy more cryptocurrency"),
        pytest.param(1, 2, "Sell all your cryptocurrency"),
        pytest.param(95, 100, "Do nothing"),
        pytest.param(99.75, 95, "Do nothing")
    ]
    )
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked, exchange_rate, current_rate, result):
    mocked.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result

