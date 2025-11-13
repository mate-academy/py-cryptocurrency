import pytest
from unittest import mock
from app.main import cryptocurrency_action

BASE_RATE = 100.0


@pytest.mark.parametrize(
    "mock_rate, current_rate, expected_action",
    [
        (110.00, BASE_RATE, "Buy more cryptocurrency"),
        (90.00, BASE_RATE, "Sell all your cryptocurrency"),
        (105.00, BASE_RATE, "Do nothing"),
        (95.00, BASE_RATE, "Do nothing"),
        (102.00, BASE_RATE, "Do nothing"),
        (98.00, BASE_RATE, "Do nothing"),
    ],
)
@mock.patch('app.main.get_exchange_rate_prediction')
def test_cryptocurrency_action_scenarios(
        mock_get_prediction,
        mock_rate: float,
        current_rate: float,
        expected_action: str
) -> None:
    mock_get_prediction.return_value = mock_rate
    actual_action = cryptocurrency_action(current_rate)
    assert actual_action == expected_action
    mock_get_prediction.assert_called_once_with(current_rate)
