import unittest.mock

import pytest
from unittest import mock

from app.main import cryptocurrency_action, Union


@pytest.fixture()
def mocked_exchange() -> unittest.mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        yield mock_exchange


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            2, 3, "Buy more cryptocurrency",
            id="value is more 1.05"
        ),
        pytest.param(
            2, 1.5, "Sell all your cryptocurrency",
            id="value is less 0.95"
        ),
        pytest.param(
            3, 3, "Do nothing",
            id="value in range (0.95, 1.05)"
        ),
        pytest.param(
            2, 1.9, "Do nothing",
            id="value is 0.95"
        ),
        pytest.param(
            3, 3.15, "Do nothing",
            id="value is 1.05"
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_exchange: unittest.mock.Mock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected: str
) -> None:
    mocked_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
