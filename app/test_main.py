import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected",
    [
        pytest.param(1, 0.95, "Do nothing",
                     id="You should not sell cryptocurrency"),
        pytest.param(1, 1.05, "Do nothing",
                     id="You should not buy cryptocurrency"),
        pytest.param(4, 2, "Sell all your cryptocurrency",
                     id="if predicted exchange rate is more than 5% lower "
                        "from the current."),
        pytest.param(2, 4, "Buy more cryptocurrency",
                     id="if predicted exchange rate is more than 5% higher "
                        "from the current."),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")  
def test_cryptocurrency_action(mocked_func,
                               current_rate,
                               exchange_rate,
                               expected):
    mocked_func.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
