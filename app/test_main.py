import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


current_rate = 10


@pytest.mark.parametrize(
    "predictable_rate, result",
    [
        (current_rate * 0.94, "Sell all your cryptocurrency"),
        (current_rate * 1.06, "Buy more cryptocurrency"),
        (current_rate * 0.95, "Do nothing"),
        (current_rate * 1.05, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        predictable_rate: Union[int, float],
        result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predictable_rate
    ) as mock_action:
        assert cryptocurrency_action(current_rate) == result
        mock_action.assert_called_once_with(current_rate)
