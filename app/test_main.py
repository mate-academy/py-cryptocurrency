from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
        (200, 210, "Do nothing"),
        (200, 190, "Do nothing"),
        (50, 60, "Buy more cryptocurrency"),
        (50, 40, "Sell all your cryptocurrency"),
        (50, 52, "Do nothing"),
        (50, 48, "Do nothing"),
        (1000, 1100, "Buy more cryptocurrency"),
        (1000, 900, "Sell all your cryptocurrency"),
        (1000, 1000, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate: int | float,
    predicted_rate: int | float,
    expected: str
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate
    ) as mock_prediction:
        result = cryptocurrency_action(current_rate)

        assert result == expected
        mock_prediction.assert_called_once_with(current_rate)
