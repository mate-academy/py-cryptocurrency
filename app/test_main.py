import pytest
from unittest.mock import Mock, patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency",
            id="Increase more than 5%"
        ),
        pytest.param(
            100, 94, "Sell all your cryptocurrency",
            id="Decrease more than 5%"
        ),
        pytest.param(
            100, 100, "Do nothing",
            id="No change"
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="Increase slightly less than 5%"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="Decrease slightly more than 5%"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="Decrease exactly 5%"
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="Increase exactly 5%"
        ),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Mock,
        current_rate: float,
        predicted_rate: float,
        expected_action: str) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected_action
