import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate_prediction() -> mock.Mock:
    with (mock.patch("app.main.get_exchange_rate_prediction") as
          mock_get_exchange):
        yield mock_get_exchange


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        pytest.param(106, 100, "Sell all your cryptocurrency",
                     id="Sell if exchange rate less than current rate"),
        pytest.param(100, 106, "Buy more cryptocurrency",
                     id="Buy if exchange rate greater than current rate"),
        pytest.param(1, 0.95, "Do nothing",
                     id="Do nothing if exchange rate more than "
                        "current rate at 5%"),
        pytest.param(100, 105, "Do nothing",
                     id="Do nothing if exchange rate is less than "
                        "current rate at 5%"),
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        exchange_rate: int | float,
        result: int | float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result
