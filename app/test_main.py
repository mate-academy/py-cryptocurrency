import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current_rate, expected",
    [
        pytest.param(
            3,
            2,
            "Buy more cryptocurrency",
            id="Should predict to buy Matecoin"
        ),
        pytest.param(
            2,
            3,
            "Sell all your cryptocurrency",
            id="Should predict to sell Matecoin"
        ),
        pytest.param(
            2.1,
            2,
            "Do nothing",
            id="Should do nothing when rate is 1.05 percent)"
        ),
        pytest.param(
            1.9,
            2,
            "Do nothing",
            id="Should do nothing when rate is 0.95 percent)"
        ),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_exchange_func,
    exchange_rate,
    current_rate,
    expected
):
    mocked_exchange_func.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == expected
