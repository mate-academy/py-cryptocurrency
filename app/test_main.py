import pytest
from typing import Union
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected_result",
    [
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (2.25, 1.35, "Sell all your cryptocurrency"),
        (1.25, 2.35, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_function: callable,
        current_rate: Union[int, float],
        prediction: Union[int, float],
        expected_result: str
) -> None:
    mock_function.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
