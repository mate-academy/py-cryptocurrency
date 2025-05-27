from unittest import mock
from unittest.mock import MagicMock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 102.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_based_on_prediction(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_action: str) -> None:

    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action