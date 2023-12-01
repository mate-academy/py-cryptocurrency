from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate: Union[int, float], "
    "cryptocurrency_activity: Union[int, float], "
    "expected_result: str",
    [
        (1.05, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.94, 1.0, "Sell all your cryptocurrency")

    ]
)
def test_cryptocurrency_action(
        prediction_rate: Union[int, float],
        cryptocurrency_activity: Union[int, float],
        expected_result: str) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = prediction_rate
        result = cryptocurrency_action(cryptocurrency_activity)
        assert result == expected_result
