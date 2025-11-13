import pytest
from unittest import mock
from unittest.mock import Mock
from app.main import cryptocurrency_action

base_rate = 100.0


@pytest.mark.parametrize(
    "mock_rate, current_rate, expected_action",
    [
        (110.00, base_rate, "Buy more cryptocurrency"),
        (90.00, base_rate, "Sell all your cryptocurrency"),
        (105.00, base_rate, "Do nothing"),
        (95.00, base_rate, "Do nothing"),
        (102.00, base_rate, "Do nothing"),
        (98.00, base_rate, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_scenarios(
        mock_get_prediction: Mock,
        mock_rate: float,
        current_rate: float,
        expected_action: str
) -> None:
    mock_get_prediction.return_value = mock_rate
    actual_action = cryptocurrency_action(current_rate)
    assert actual_action == expected_action
    mock_get_prediction.assert_called_once_with(current_rate)
