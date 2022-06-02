from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "predicted_rate, current_rate, outcome",
    [
        pytest.param(
            4,
            1,
            "Buy more cryptocurrency",
            id="Good outcome"
        ),
        pytest.param(
            0.1,
            1,
            "Sell all your cryptocurrency",
            id="Bad outcome"
        ),
        pytest.param(
            1.05,
            1,
            "Do nothing",
            id="Top don't care outcome"
        ),
        pytest.param(
            0.95,
            1,
            "Do nothing",
            id="Low don't care outcome"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_predict_outcome(mocked_prediction,
                         predicted_rate,
                         current_rate,
                         outcome):
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == outcome
