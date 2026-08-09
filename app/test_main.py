import pytest
from typing import Union
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (100, 90, "Sell all your cryptocurrency"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
