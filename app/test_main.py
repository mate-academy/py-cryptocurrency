from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        # Більше ніж на 5% вище -> Buy more cryptocurrency
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 120, "Buy more cryptocurrency"),
        (200, 400, "Buy more cryptocurrency"),

        # Більше ніж на 5% нижче -> Sell all your cryptocurrency
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 80, "Sell all your cryptocurrency"),
        (200, 100, "Sell all your cryptocurrency"),

        # В межах +-5% (включно з граничними значеннями) -> Do nothing
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float, predicted_rate: float, expected_result: str
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ) as mocked_prediction:
        result = cryptocurrency_action(current_rate)

    mocked_prediction.assert_called_once_with(current_rate)
    assert result == expected_result
