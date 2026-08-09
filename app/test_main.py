from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, simulated_prediction, expected_action",
    [
        (100.0, 110.0, "Buy more cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 102.0, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_scenarios(
    mock_prediction: MagicMock,
    current_rate: float,
    simulated_prediction: float,
    expected_action: str
) -> None:

    mock_prediction.return_value = simulated_prediction

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
    mock_prediction.assert_called_once_with(current_rate)
