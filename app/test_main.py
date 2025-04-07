from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "prediction_value, current_rate, result",
    [
        (5.82, 5, "Buy more cryptocurrency"),
        (4.12, 6.42, "Sell all your cryptocurrency"),
        (7.12, 7.08, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_choice(
        rate_prediction: int | float,
        prediction_value: int | float,
        current_rate: int | float,
        result: str
) -> None:
    rate_prediction.return_value = prediction_value
    assert cryptocurrency_action(current_rate) == result
