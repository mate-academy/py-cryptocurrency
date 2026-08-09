from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,exception_message",
    [
        pytest.param(
            3,
            2,
            "Buy more cryptocurrency",
        ),
        pytest.param(
            1.05,
            1,
            "Do nothing",
        ),
        pytest.param(
            0.95,
            1,
            "Do nothing",
        ),
        (
            1,
            1,
            "Do nothing",
        ),
        (
            1,
            2,
            "Sell all your cryptocurrency",
        )
    ]
)
def test_get_cryptocurrency(
        prediction_rate: int,
        current_rate: int,
        exception_message: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_rate_prediction:
        mocked_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == exception_message
