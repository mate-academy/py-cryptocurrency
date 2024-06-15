from unittest import mock
import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, prediction_rate, return_value",
    [
        (1, 1.0, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 1.06, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(mock_exchange_rate_prediction: mock,
                               current_rate: int | float,
                               prediction_rate: int | float,
                               return_value: str) -> None:
    mock_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == return_value
