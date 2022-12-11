import pytest

from unittest import mock
from random import uniform

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,action",
    [
        pytest.param(
            1,
            1.06,
            "Buy more cryptocurrency",
            id="for more 5%"
        ),
        pytest.param(
            1,
            0.94,
            "Sell all your cryptocurrency",
            id="for lower 5%"
        ),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="difference is not that much min value"
        ),
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="difference is not that much max value"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock.Mock,
        current_rate: int,
        prediction_rate: float,
        action: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == action
