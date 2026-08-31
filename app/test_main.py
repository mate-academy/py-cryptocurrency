from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current, prediction, result",
    [
        pytest.param(
            1.00, 1.06,
            "Buy more cryptocurrency",
            id="buy",
        ),
        pytest.param(
            1.00, 0.94,
            "Sell all your cryptocurrency",
            id="sell",
        ),
        pytest.param(
            1.00, 1.01,
            "Do nothing",
            id="small increase",
        ),
        pytest.param(
            1.00, 0.98,
            "Do nothing",
            id="small decrease",
        ),
        pytest.param(
            1.00, 1.05,
            "Do nothing",
            id="buy boundary",
        ),
        pytest.param(
            1.00, 0.95,
            "Do nothing",
            id="sell boundary",
        ),
    ],
)
def test_cryptocurrency_action(
    current: float,
    prediction: float,
    result: str,
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mock:
        prediction_mock.return_value = prediction

        actual_result = cryptocurrency_action(current)

        assert actual_result == result
