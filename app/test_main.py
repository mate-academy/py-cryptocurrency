import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, outcome",
    [
        (
            1, 0.9, "Buy more cryptocurrency"
        ),
        (
            1.05, 1, "Do nothing"
        ),
        (
            1, 2, "Sell all your cryptocurrency"
        ),
        (
            0.95, 1, "Do nothing"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_function(
        mocked_func,
        prediction_rate,
        current_rate,
        outcome
):
    mocked_func.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == outcome
