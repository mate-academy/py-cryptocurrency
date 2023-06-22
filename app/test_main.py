from typing import Callable
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", create=True)
def test_cryptocurrency_action_should_do_nothing(
        mocked_get_rate: Callable
) -> None:
    mocked_get_rate.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing", (
        "You should do nothing your rate == 95%"
    )

    mocked_get_rate.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing", (
        "You should do nothing your rate == 105%"
    )
