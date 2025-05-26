from unittest import mock
from .main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, result",
    [
        (0.94, "Sell all your cryptocurrency"),
        (0.96, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange(mock_get_exchange_rate_prediction: mock,
                      current_rate: float,
                      result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = current_rate
    assert cryptocurrency_action(1.0) == result
