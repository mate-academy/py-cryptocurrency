from unittest.mock import Mock, patch
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "mocked_value, current_rate, expected_result",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.8, 1.0, "Sell all your cryptocurrency"),
        (1.04, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (1.05, 1.0, "Do nothing")
    ],
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Mock,
        mocked_value: float,
        current_rate: float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = mocked_value

    assert cryptocurrency_action(current_rate) == expected_result
