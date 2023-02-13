from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_increase_prediction(mocked_transfer: Any) -> None:
    mocked_transfer.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_decrease_prediction(mocked_transfer: Any) -> None:
    mocked_transfer.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
