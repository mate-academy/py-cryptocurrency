from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,current_rate, expected",
    [
        pytest.param(
            1.41,
            1.5,
            "Sell all your cryptocurrency",
            id="Test prediction rate decrease"
        ),
        pytest.param(
            1.59,
            1.5,
            "Buy more cryptocurrency",
            id="Test prediction rate increase"
        ),
        pytest.param(
            1.47,
            1.4,
            "Do nothing",
            id="Test without changes (test 1.05 bound)"
        ),
        pytest.param(
            1.52,
            1.6,
            "Do nothing",
            id="Test without changes (test 0.95 bound)"
        ),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: float,
        exchange_rate: float,
        current_rate: float,
        expected: str
) -> None:
    mocked_exchange_rate.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == expected
