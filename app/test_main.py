import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 102, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 98, "Do nothing"),
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_prediction: mock.Mock,
        current_rate: int,
        predicted_rate: int,
        expected_action: str) -> None:
    mock_get_prediction.return_value = predicted_rate

    action = cryptocurrency_action(current_rate)

    assert action == expected_action
