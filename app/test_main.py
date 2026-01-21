from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate,prediction,expected_result",
    [
        pytest.param(
            100,
            120,
            "Buy more cryptocurrency",
            id="Buy more cryptocurrency if prediction/rate more than 1.05"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="Do nothing if prediction/rate is 1.05"
        ),
        pytest.param(
            100,
            80,
            "Sell all your cryptocurrency",
            id="Sell all your cryptocurrency if prediction/rate less than 0.95"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="Do nothing if prediction/rate is 0.95"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="Do nothing if difference not that much"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: callable,
        rate: int | float,
        prediction: int | float,
        expected_result: str
) -> None:
    mocked_rate_prediction.return_value = prediction
    assert cryptocurrency_action(rate) == expected_result
