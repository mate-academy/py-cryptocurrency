import pytest
from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        pytest.param(1.06, 1, "Buy more cryptocurrency"),
        pytest.param(0.94, 1, "Sell all your cryptocurrency"),
        pytest.param(1.05, 1, "Do nothing"),
        pytest.param(0.95, 1, "Do nothing")
    ],
)
def test_cryptocurrency_action(
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
