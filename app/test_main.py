import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 1.9, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 0.3, "Sell all your cryptocurrency"),
        (1, 0.8, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        mock_rate: mock,
        current_rate: int,
        predicted_rate: float,
        expected_result: str,
) -> None:
    mock_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
