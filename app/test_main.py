import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        yield mock_exchange


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            2, 5, "Buy more cryptocurrency",
            id="check exception when value more than 1.05"
        ),
        pytest.param(
            2, 1.5, "Sell all your cryptocurrency",
            id="check exception when value less than 0.95"
        ),
        pytest.param(
            2, 2, "Do nothing",
            id="check value in range (0.95, 1.05)"
        ),
        pytest.param(
            2, 1.9, "Do nothing",
            id="check value is 0.95"
        ),
        pytest.param(
            2, 2.1, "Do nothing",
            id="check value is 1.05"
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_exchange,
        current_rate,
        prediction_rate,
        expected
):
    mocked_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
