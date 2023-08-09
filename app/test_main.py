from unittest import mock

from typing import Union

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "test_current_rate,test_exchange_rate,expected_result",
    [
        (1, 1.1, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        test_current_rate: Union[int, float],
        test_exchange_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=test_exchange_rate):
        assert cryptocurrency_action(test_current_rate) == expected_result
