from app.main import cryptocurrency_action
from unittest import mock
import pytest


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, message",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.01, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
    ]
)
def test_cannot_access_if_only_valid_url(mocked_func: mock,
                                         current_rate: int,
                                         predicted_rate: int,
                                         message: str) -> None:
    mocked_func.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == message
