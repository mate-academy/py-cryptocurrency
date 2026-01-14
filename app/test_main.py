import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action

test_cases = [
    (100.00, 105.01, "Buy more cryptocurrency"),
    (100.00, 105.00, "Do nothing"),
    (100.00, 100.00, "Do nothing"),
    (100.00, 95.00, "Do nothing"),
    (100.00, 94.99, "Sell all your cryptocurrency"),
    (50.00, 52.51, "Buy more cryptocurrency"),
    (50.00, 47.49, "Sell all your cryptocurrency"),
]


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    test_cases
)
def test_cryptocurrency_action_boundary_conditions(
        mock_get_exchange_rate_prediction: any,
        current_rate: any,
        predicted_rate: any,
        expected_action: any
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
    mock_get_exchange_rate_prediction.assert_called_once_with(current_rate)
