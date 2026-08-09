from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


def test_when_exchange_rate_is_lower_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        current_rate = 100.0
        predicted_rate = 0.94 * current_rate
        mocked_rate.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"


def test_when_exchange_rate_is_higher_from_the_current() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        current_rate = 100.0
        predicted_rate = 1.06 * current_rate
        mocked_rate.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"


@pytest.mark.parametrize("changed_param", [0.95, 0.96, 1.04, 1.05])
def test_when_difference_is_not_that_much(
        changed_param: Union[int, float]
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        current_rate = 100.0
        predicted_rate = changed_param * current_rate
        mocked_rate.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)

        assert result == "Do nothing"
