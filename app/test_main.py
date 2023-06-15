import pytest
from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,rate_prediction,expected_result",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency",
            id=("should return 'Buy more...' when predicted rate"
                " is more than 5% higher from the current")
        ),
        pytest.param(
            100, 94, "Sell all your cryptocurrency",
            id=("should return 'Sell all...' when predicted rate"
                " is more than 5% lower from the current")
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="should return 'Do nothing' if difference is not that much"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="should return 'Do nothing' if difference is not that much"
        )
    ]
)
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: Callable,
                               current_rate: int | float,
                               rate_prediction: int | float,
                               expected_result: str,) -> None:
    mock_get_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == expected_result
