import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, future_rate, expected_result",
    [
        pytest.param(1.0, 1.05, "Do nothing",
                     id="Under 1.05"),
        pytest.param(1.0, 1.06, "Buy more cryptocurrency",
                     id="Upper 1.05"),
        pytest.param(1.0, 0.95, "Do nothing",
                     id="Upper 0.95"),
        pytest.param(1.0, 0.94, "Sell all your cryptocurrency",
                     id="Under 0.95"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_return_proper_respond(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float,
        future_rate: float,
        expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = future_rate
    assert cryptocurrency_action(current_rate) == expected_result
