import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, mock_prediction_result, expected",
    [
        pytest.param(
            100,
            94.99,
            "Sell all your cryptocurrency",
            id="should sell if `prediction` < `current` * 0.95"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="should do nothing if `prediction` > `current` * 0.95"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="should do nothing if `prediction` < `current` * 1.05"
        ),
        pytest.param(
            100,
            105.01,
            "Buy more cryptocurrency",
            id="should buy if `prediction` > `current` * 1.05"
        ),
    ]
)
def test_cryptocurrency_action(
    mocked_exchange_rate_prediction,
    current_rate,
    mock_prediction_result,
    expected
):
    mocked_exchange_rate_prediction.return_value = mock_prediction_result
    assert cryptocurrency_action(current_rate) == expected
