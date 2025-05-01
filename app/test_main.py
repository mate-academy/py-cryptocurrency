from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 94.1, "Sell all your cryptocurrency"),
        (100, 104.9, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    action = cryptocurrency_action(current_rate)
    assert action == expected_action
