from unittest import mock

from app.main import cryptocurrency_action

import pytest


@pytest.mark.parametrize(
    "predicted_rate, expected_result",
    [
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="should advice to sell when prediction is < 0.95"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="should advice to wait when prediction is from 0.95 to 1.05"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="should advice to wait when prediction is from 0.95 to 1.05"
        ),
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="should advice to buy more currency when prediction > 1.05"
        )
    ]
)
def test_should_advice_correctly(
        predicted_rate: float,
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as \
            mocked_prediction:
        mocked_prediction.return_value = predicted_rate
        assert cryptocurrency_action(1) == expected_result
