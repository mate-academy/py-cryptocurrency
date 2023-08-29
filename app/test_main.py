import pytest

from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_action: str
) -> None:
    with (
        mock.patch("get_exchange_rate_prediction") as
        mocked_get_exchange_rate_prediction
    ):
        mocked_get_exchange_rate_prediction.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == expected_action
