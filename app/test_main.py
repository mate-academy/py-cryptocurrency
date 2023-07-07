from typing import Callable
from unittest import mock
from .main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_is_func_do_not_by_crypto_correct(mocked_exchange_rate_prediction: Callable) -> None:
    mocked_exchange_rate_prediction.return_value = 1.0

    result = cryptocurrency_action(current_rate=1.0)

    assert result is "Do nothing"
    mocked_exchange_rate_prediction.assert_called_once_with(1.0)


