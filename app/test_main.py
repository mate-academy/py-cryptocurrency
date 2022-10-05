from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


@pytest.mark.parametrize(
    "current_rate, predicted_exchange_rate, expected",
    [
        pytest.param(
            5,
            5.5,
            "Buy more cryptocurrency",
            id="rate is more than 5% higher"
        ),
        pytest.param(
            5,
            4.5,
            "Sell all your cryptocurrency",
            id="rate is more than 5% lower"
        ),
        pytest.param(
            5,
            5.25,
            "Do nothing",
            id="minor profit"
        ),
        pytest.param(
            5,
            4.75,
            "Do nothing",
            id="minor loss"
        ),
    ]
)
def test_cryptocurrency(
        mocked_rate: int | float,
        current_rate: int | float,
        predicted_exchange_rate: int | float,
        expected: str
) -> None:
    mocked_rate.return_value = predicted_exchange_rate
    assert cryptocurrency_action(current_rate) == expected
