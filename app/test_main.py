from unittest import mock
import pytest
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_status",
    [
        pytest.param(100, 110, "Buy more cryptocurrency"),
        pytest.param(120, 110, "Sell all your cryptocurrency"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(105, 100, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_logic(
        mocked_rate_prediction: object,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_status: str,

) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_status
