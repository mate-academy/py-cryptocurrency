from unittest import mock
from typing import Union

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        pytest.param(2.11, 2.0, "Buy more cryptocurrency"),
        pytest.param(2.10, 2.0, "Do nothing"),
        pytest.param(1.9, 2.0, "Do nothing"),
        pytest.param(1.89, 2.0, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: float,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
