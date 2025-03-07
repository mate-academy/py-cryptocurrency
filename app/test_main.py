import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_exchange() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        pytest.param(
            1,
            1.06,
            "Buy more cryptocurrency",
            id="predicted rate more higher 5%"
        ),
        pytest.param(
            1,
            0.94,
            "Sell all your cryptocurrency",
            id="predicted rate more lower 5%"
        ),
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="predicted rate higher with low profit"
        ),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="predicted rate lower with low loss"
        )
    ]
)
def test_cryptocurrency_action(mocked_exchange: int | float,
                               current_rate: int | float,
                               exchange_rate: int | float,
                               expected: str) -> None:
    mocked_exchange.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
