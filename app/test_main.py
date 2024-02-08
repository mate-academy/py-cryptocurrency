from app.main import cryptocurrency_action
from unittest import mock
import pytest


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "curent_rate, predicted_rate, message",
    [
        (6000, 10000, "Buy more cryptocurrency"),
        (6000, 1000, "Sell all your cryptocurrency"),
        (1000, 1000, "Do nothing"),
    ]
)
def test_cannot_access_if_only_valid_url(mocked_func: mock,
                                         curent_rate: int,
                                         predicted_rate: int,
                                         message: str) -> None:
    mocked_func.return_value = predicted_rate
    assert cryptocurrency_action(curent_rate) == message
