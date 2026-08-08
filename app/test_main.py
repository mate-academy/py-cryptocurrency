from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, message",
    [
        pytest.param(
            5,
            6,
            "Buy more cryptocurrency",
            id="Should tell to buy more"
        ),
        pytest.param(
            5,
            4,
            "Sell all your cryptocurrency",
            id="Should tell to sell all"
        ),
        pytest.param(
            5,
            5.01,
            "Do nothing",
            id="Should tell to do nothing"
        ),
        pytest.param(
            5,
            5.25,
            "Do nothing",
            id="Should tell to do nothing"
        ),
        pytest.param(
            5,
            4.75,
            "Do nothing",
            id="Should tell to do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_correct_action_advice(
        mocked_predictor,
        current_rate,
        prediction_rate,
        message
):
    mocked_predictor.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == message
