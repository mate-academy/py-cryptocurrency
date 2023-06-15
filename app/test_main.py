from typing import Callable
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_105(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
