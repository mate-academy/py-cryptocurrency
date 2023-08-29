import pytest

from unittest import mock
from typing import Union, Callable

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: Callable,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_action: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_action
