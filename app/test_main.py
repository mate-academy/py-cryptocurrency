import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, action", [
        (5.1, 5.2, "Do nothing"),
        (5, 2.5, "Buy more cryptocurrency"),
        (2.5, 5, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: callable,
        prediction_rate: int | float,
        current_rate: int | float,
        action: str
) -> None:
    mock_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == action
