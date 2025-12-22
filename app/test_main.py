import pytest
from typing import Union
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 105, "Do nothing"),
        (100, 105.0001, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 94.9999, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
