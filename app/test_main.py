# write your code here
import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, result",
    [
            (106, "Buy more cryptocurrency"),
            (94, "Sell all your cryptocurrency"),
            (95, "Do nothing"),
            (105, "Do nothing"),
    ])
def test_cryptocurrency_action(current_rate: Union[int, float], result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        mocked_rate.return_value = current_rate
        assert cryptocurrency_action(100) == result
