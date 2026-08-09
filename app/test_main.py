from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        # Buy more cryptocurrency (> +5%)
        (100, 106, "Buy more cryptocurrency"),
        (200, 220, "Buy more cryptocurrency"),

        # Sell all your cryptocurrency (< -5%)
        (100, 94, "Sell all your cryptocurrency"),
        (200, 180, "Sell all your cryptocurrency"),

        # Do nothing (within ±5%)
        (100, 105, "Do nothing"),  # exactly +5%
        (100, 95, "Do nothing"),   # exactly -5%
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: mock.Mock,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected
    mock_prediction.assert_called_once_with(current_rate)
