import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate_mock, prediction_rate, expected_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: None,
        current_rate_mock: int | float,
        prediction_rate: int | float,
        expected_result: str) -> None:
    mocked_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate_mock)
    assert result == expected_result
