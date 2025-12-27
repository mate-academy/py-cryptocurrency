import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "actual_rate,predicted_rate,expected_result",
    [
        pytest.param(100, 120, "Buy more cryptocurrency"),
        pytest.param(100, 80, "Sell all your cryptocurrency"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),
    ],
    ids=[
        "Buy more cryptocurrency if predicted exchange rate "
        "is more than 5% higher from the current.",
        "Sell all your cryptocurrency, if predicted exchange rate "
        "is more than 5% lower from the current.",
        "Do nothing, if prediction_rate / current_rate == 1.05",
        "Do nothing, if prediction_rate / current_rate == 0.95."
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: callable,
        actual_rate: int | float,
        predicted_rate: int | float,
        expected_result: str
) -> None:
    mocked_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(actual_rate) == expected_result
