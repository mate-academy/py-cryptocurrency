from unittest import mock
from typing import Union
import pytest
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "today_rate, tomorrow_rate, expected_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_function: mock,
        today_rate: Union[int, float],
        tomorrow_rate: Union[int, float],
        expected_result: str,
) -> None:
    mocked_function.return_value = tomorrow_rate
    assert cryptocurrency_action(today_rate) == expected_result
