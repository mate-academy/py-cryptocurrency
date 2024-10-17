from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction: Any) -> None:
    cryptocurrency_action(1)
    mocked_prediction.assert_called_once()
