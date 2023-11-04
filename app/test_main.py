import pytest
from unittest import mock
from typing import Union

from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,pred_rate,expected_result",
    [
        (20, 30, "Buy more cryptocurrency"),
        (20, 21.5, "Buy more cryptocurrency"),
        (12, 2, "Sell all your cryptocurrency"),
        (12, 11.3, "Sell all your cryptocurrency"),
        (44, 45, "Do nothing"),
        (44, 43, "Do nothing"),
    ]
)
def test_get_exchange_rate_prediction(
        current_rate: Union[int, float],
        pred_rate: Union[int, float],
        expected_result: str
) -> None:
    rate_pred = "app.main.get_exchange_rate_prediction"
    with mock.patch(rate_pred, return_value=pred_rate) as mocked_rate_pred:
        assert cryptocurrency_action(current_rate) == expected_result
        mocked_rate_pred.assert_called_once_with(current_rate)
