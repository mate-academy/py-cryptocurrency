from unittest import mock

import app.main
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_inner_function_call(
        mocked_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    cryptocurrency_action(2)
    mocked_get_exchange_rate_prediction.assert_called_once_with(2)
