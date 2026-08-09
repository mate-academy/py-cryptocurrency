from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        pytest.param(
            41.2,
            45.2,
            "Buy more cryptocurrency",
            id="test when prediction much bigger"
        ),
        pytest.param(
            41.2,
            41.4,
            "Do nothing",
            id="test when prediction bit bigger"
        ),
        pytest.param(
            32.7,
            12.5,
            "Sell all your cryptocurrency",
            id="test when prediction much lower"
        ),
        pytest.param(
            41.2,
            41.1,
            "Do nothing",
            id="test when prediction bit lower"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="test when prediction decreased by 5%"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="test when prediction increased by 5%"
        )
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_get:
        mocked_get.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
