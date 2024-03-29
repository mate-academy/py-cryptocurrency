import pytest
from unittest import mock
from typing import Callable, Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "exchange_rate_prediction, current_rate, expected_result",
    [
        (73.85, 73, "Do nothing"),
        (17.62, 50, "Sell all your cryptocurrency"),
        (1364.54, 220.5, "Buy more cryptocurrency"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Callable,
        exchange_rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate_prediction
    assert cryptocurrency_action(current_rate) == expected_result
