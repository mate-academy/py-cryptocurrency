import pytest
from unittest.mock import patch
from typing import Callable
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "test_rate,expected_result",
    [
        pytest.param(0.94, "Sell all your cryptocurrency"),
        pytest.param(0.95, "Do nothing"),
        pytest.param(1.05, "Do nothing"),
        pytest.param(1.06, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate_prediction: Callable,
        test_rate: float,
        expected_result: str
) -> None:
    mock_rate_prediction.return_value = test_rate
    assert cryptocurrency_action(1) == expected_result
