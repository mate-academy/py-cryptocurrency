from unittest import mock
from app.main import cryptocurrency_action
import pytest
from typing import Union


@pytest.mark.parametrize("exchange_rate, current_rate, result", [
    (1.06, 1, "Buy more cryptocurrency"),
    (0.94, 1, "Sell all your cryptocurrency"),
    (1.05, 1, "Do nothing"),
    (0.95, 1, "Do nothing"),
])
def test_cryptocurrency_action(
        exchange_rate: Union[int, float],
        current_rate: Union[int, float],
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mocked_exchange_rate:
        mocked_exchange_rate.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
